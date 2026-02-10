from sqlalchemy import Column, String, Boolean, Integer, Date, DateTime
from app.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship
from enum import Enum
from sqlalchemy import Enum as SQLAlchemyEnum

class UserRole(str, Enum):
    CLIENTE = "cliente"
    VENDEDOR = "vendedor"
    ADMIN = "admin"
    
class UserDB(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True, nullable=True)
    birthdate = Column(Date, nullable=True) 
    hashed_password = Column(String)
    role = Column(SQLAlchemyEnum(UserRole), default=UserRole.CLIENTE, nullable=False)
    disabled = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    @property
    def is_active(self) -> bool:
        return not self.disabled