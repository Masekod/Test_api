from pydantic import BaseModel, EmailStr, ConfigDict
from typing import List, Union, Optional


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
    message: Union[str, List[str]]
    error: Optional[str] = None
    statusCode: int

    model_config = ConfigDict(extra="ignore")

class AuthUnauthorizedResponse(BaseModel):
    message: str
    statusCode: int