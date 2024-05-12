from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    name: str
    password: str


class UserAuth(UserBase):
    password: str


class User(UserBase):
    id: int
    name: str
    tg_username: str | None

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
