from pydantic import BaseModel, RootModel
from typing import List


class TodosRequest(BaseModel):
    title: str
    description: str
    date: str
    time: str
    checked: bool


class TodosSuccessResponse(BaseModel):
    title: str
    description: str
    date: str
    time: str
    checked: bool
    id: int
    userId: int


class TodosBadRequestResponse(BaseModel):
    error: str
    statusCode: int
    message: int


class TodosUnauthorizedResponse(BaseModel):
    error: str
    statusCode: int
    message: int
