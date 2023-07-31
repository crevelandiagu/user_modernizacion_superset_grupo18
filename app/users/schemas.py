from sqlalchemy import Column, String, Boolean
from uuid import uuid4
from app.config.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    username = Column(String(20))
    email = Column(String(100))
    first_name = Column(String(50))
    last_name = Column(String(50))
    is_active = Column(Boolean, default=True)
    is_anonymous = Column(Boolean, default=True)

    def serializer(self):
        return {
                "id": self.id,
                "username": self.username,
                "email": self.email,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "is_active": self.is_active,
                "is_anonymous": self.is_anonymous
            }
