from typing import List, Union

from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class UserInfo(BaseModel):
    username: str
    password: str
    email: EmailStr


class UserInDB(UserInfo):
    hashed_password: str

class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    password: str


class UserList(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True

class EmailSchema(BaseModel):
   email: List[EmailStr]