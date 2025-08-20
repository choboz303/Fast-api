from datetime import datetime, timedelta

import jwt
from decouple import config
from fastapi import HTTPException
from passlib.context import CryptContext

JWT_KEY = config("JWT_KEY")


class AuthJwtCsrf:
    pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret_key = JWT_KEY

    def generate_hashed_pw(self, password) -> str:
        return
