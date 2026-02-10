from pydantic import BaseModel
from app.schemas.favorite import FavoriteRead
from typing import List
from app.schemas.conversation import ConversationInfoOut
from enum import Enum
from typing import Optional

class UserRole(str, Enum):
    CLIENTE = "cliente"
    VENDEDOR = "vendedor"
    ADMIN = "admin"
    
class UserCreate(BaseModel):
    username: str
    password: str
    
class UserOut(BaseModel):
    id: int
    username: str
    email: Optional[str] = None
    role: UserRole
    disabled: bool
    favorites: List[FavoriteRead] = []
    conversations: List[ConversationInfoOut] = []

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    role: Optional[UserRole] = None
    disabled: Optional[bool] = None

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
