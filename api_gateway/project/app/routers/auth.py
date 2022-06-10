from . import User, Token, authenticator, grpc_consumer

import grpc
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(tags=['Auth'])


@router.post('/register')
async def register(new_user: User) -> dict:

    hashed_password = authenticator.get_password_hash(new_user.password)
    new_user.is_active = True

    try:
        user = await grpc_consumer.create_user(username=new_user.username,
                                               full_name=new_user.full_name,
                                               email=new_user.email,
                                               hashed_password=hashed_password,
                                               created_at=new_user.created_at,
                                               is_active=new_user.is_active,
                                               is_verified=new_user.is_verified)
        return user

    except grpc.RpcError as e:
        if e.code().name == "ALREADY_EXISTS":
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail='User is already registered')


@router.post('/login', response_model=Token)
async def login_for_access_token(user_credentials: OAuth2PasswordRequestForm = Depends()) -> dict:

    exception_credentials = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail='Incorrect username or password',
                                          headers={'WWW-Authenticate': 'Bearer'})

    try:
        curr_user = await grpc_consumer.get_user_by_username(username=user_credentials.username)
        verified_password = authenticator.verify_password(user_credentials.password, curr_user.hashed_password)

        # Raise exception if password is not correct or user is inactive
        if not (verified_password and curr_user.consumer_status.is_active):
            raise exception_credentials

        access_token = authenticator.create_access_token(data={'sub': curr_user.username})

        # Update consumer status
        await grpc_consumer.update_status(username=user_credentials.username, is_active=True, is_verified=True)

        return {'access_token': access_token, 'token_type': 'bearer'}
    except grpc.RpcError as e:
        if e.code().name == 'NOT_FOUND':
            raise exception_credentials
