from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class User(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class PermitApplicationCreate(BaseModel):
    permit_type: str

class PermitApplication(BaseModel):
    id: int
    user_id: int
    permit_type: str
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Add other schemas here as needed...