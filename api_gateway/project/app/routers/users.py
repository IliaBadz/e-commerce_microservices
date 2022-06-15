from . import authenticator, grpc_consumer, User, UserOut, UpdateUser

from fastapi import APIRouter, Depends, status


router = APIRouter(prefix='/users',
                   tags=['Users'])


@router.get('/{user_id}', status_code=status.HTTP_200_OK)
async def get_user(user_id: str) -> UserOut:
    user = await grpc_consumer.get_user_by_id(user_id=user_id)
    return user


@router.put("/update", status_code=status.HTTP_200_OK)
async def update_user(user_update: UpdateUser, current_user: User = Depends(authenticator.get_current_user)):

    updated_user = await grpc_consumer.update_user(username=current_user.get('username'),
                                                   full_name=user_update.full_name,
                                                   email=user_update.email)
    return updated_user


@router.delete("/delete/")
async def delete_user(current_user: User = Depends(authenticator.get_current_user)):
    updated_user = await grpc_consumer.update_status(username=current_user.get('username'),
                                                     is_active=False,
                                                     is_verified=False)
    return updated_user
