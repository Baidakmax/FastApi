from pydantic import BaseModel, EmailStr
from typing import List

from models.core import Item


class ItemBase(BaseModel):
    title: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True


UserAuth = UserCreate


class LiteUser(UserBase):
    id: int

    class Config:
        orm_mode = True


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str

    class Config:
        orm_mode = True