from pydantic import BaseModel


class UserBase(BaseModel):
    user_name: str
    user_type: str
    document_id: int
    user_address: str
    user_phone: int


class UserCreate(UserBase):
    user_email: str
    user_password: str


class User(UserBase):
    user_email: str

    class Config:
        orm_mode = True
