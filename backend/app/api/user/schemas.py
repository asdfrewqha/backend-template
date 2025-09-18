from uuid import UUID

from pydantic import BaseModel, ConfigDict


class UserProfileResponse(BaseModel):
    id: UUID
    username: str
    name: str

    model_config = ConfigDict(arbitrary_types_allowed=True)


class UserResponse(BaseModel):
    id: UUID
    username: str
    name: str

    model_config = ConfigDict(arbitrary_types_allowed=True)
