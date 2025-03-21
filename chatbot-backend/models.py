from sqlalchemy import Column, Integer, String, JSON
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    thread_id = Column(String, nullable=True)
    thread_data= Column(JSON, nullable=True)
