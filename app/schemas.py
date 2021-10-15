from typing import List, Optional

from pydantic import BaseModel


class TagBase(BaseModel):
    name: str


class TagCreate(TagBase):
    pass


class Tag(TagBase):
    id: int
    places: List[str] = []

    class Config:
        orm_mode = True


class PlaceBase(BaseModel):
    name: str
    review: int
    city: str
    site: Optional[str] = None
    tags: List[Tag] = []


class PlaceCreate(PlaceBase):
    pass


class Place(PlaceBase):
    id: int

    class Config:
        orm_mode = True


class UserListBase(BaseModel):
    title: str
    description: str
    places: List[Place] = []


class UserListCreate(UserListBase):
    pass


class UserList(UserListBase):
    id: int
    owner: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    lists: List[UserList] = []

    class Config:
        orm_mode = True
