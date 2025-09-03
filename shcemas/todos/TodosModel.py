from pydantic import BaseModel


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
    statusCode: int
    message: str
    error: str

class TodosUnauthorizedResponse(BaseModel):
    statusCode: int
    message: str
    error: str

class TodosNotFounded(BaseModel):
    statusCode: int
    message: str
    error: str