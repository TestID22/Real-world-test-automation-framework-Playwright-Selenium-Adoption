from pydantic import BaseModel, EmailStr, HttpUrl


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    html: HttpUrl