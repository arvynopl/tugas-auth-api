# File app/database/models.py

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: EmailStr
    is_active: bool = True

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class APIKey(BaseModel):
    id: int
    user_id: int
    key: str
    name: str
    is_active: bool
    created_at: datetime
    expires_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# For login
class UserLogin(BaseModel):
    username: str
    password: str

# For token response
class Token(BaseModel):
    access_token: str
    token_type: str
    api_key: str

# For user response (without sensitive info)
class UserResponse(BaseModel):
    username: str
    email: EmailStr
    is_active: bool