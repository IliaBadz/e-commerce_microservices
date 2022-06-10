import os

from typing import Union
from datetime import datetime, timedelta

from . import routers, TokenData

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt, JWTError


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


class Authenticator:
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

    def __init__(self):
        self.pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    async def get_user(self, username: str):
        user = await routers.grpc_consumer.get_user_by_username(username)
        return user

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def create_access_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(self.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encode_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.JWT_ALGORITHM)

        return encode_jwt

    async def get_current_user(self,  token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                              detail='Could not validate credentials',
                                              headers={'WWW-Authenticate': 'Bearer'},)

        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.JWT_ALGORITHM])
            username: str = payload.get('sub')

            if username is None:
                raise credentials_exception

            token_data = TokenData(username=username)
        except JWTError:
            raise credentials_exception

        user = await self.get_user(username=token_data.username)

        return user
