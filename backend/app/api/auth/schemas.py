from uuid import UUID

from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    name: str
    username: str = Field(
        ...,
        min_length=3,
        max_length=20,
        pattern=r"^[a-zA-Z0-9_]+$",
    )
    password: str


class UserRegResponse(BaseModel):
    id: UUID


class UserLogin(BaseModel):
    identifier: str
    password: str
