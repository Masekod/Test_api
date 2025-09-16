from pydantic import BaseModel, EmailStr
from typing import List


class AuthRequest(BaseModel):
    email: EmailStr
    password: str


class User(BaseModel):
    email: EmailStr
    id: int


class AuthSuccessResponse(BaseModel):
    accessToken: str
    refreshToken: str
    user: User


class AuthBadRequestResponse(BaseModel):
    message: List[str]
    error: str
    statusCode: int


class AuthUnauthorizedResponse(BaseModel):
    message: str
    statusCode: int
