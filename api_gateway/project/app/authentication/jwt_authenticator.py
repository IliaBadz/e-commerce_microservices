from datetime import datetime, timedelta

import passlib.context

from . import settings, routers, TokenData

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt, JWTError


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


class JWTAuthenticator:
    """Provides methods to implement jwt authentication"""

    def __init__(self):
        self.pwd_context: CryptContext = CryptContext(schemes=['bcrypt'], deprecated='auto')

    async def get_user(self, username: str) -> dict:
        """
        Makes grpc request to get user
        :param str usename: Username of consumer
        :return: User credentials
        :rtype: dict
        """
        user = await routers.grpc_consumer.get_user_by_username(username)
        return user

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """
        Verifies whether provided password matches with registration password

        :param str plain_password: Password without hashing
        :param str hashed_password: Hashed password

        :returns:
            ``True`` if the password matched the hash, else ``False``.
        :rtype: bool
        """
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str):
        """Hashes plain password"""
        return self.pwd_context.hash(password)

    def create_access_token(self, data: dict) -> str:
        """Creates access token"""

        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encode_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
        return encode_jwt

    async def get_current_user(self,  token: str = Depends(oauth2_scheme)) -> dict:
        """
        Decodes jwt to get username and returns user credentials

        :param str token: JWT token.

        :return: User credentials
        :rtype: dict
        """

        credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                              detail='Could not validate credentials',
                                              headers={'WWW-Authenticate': 'Bearer'},)

        try:
            payload: dict = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            username: str = payload.get('sub')

            if username is None:
                raise credentials_exception

            token_data = TokenData(username=username)
        except JWTError as e:
            raise credentials_exception

        user = await self.get_user(username=token_data.username)

        return user
