from sqlalchemy import Column, Integer, String

from database import Base
from settings import NAME_LENGHT


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(length=NAME_LENGHT),
                      unique=True, index=True, nullable=False)
    name = Column(String(length=NAME_LENGHT), nullable=False)
    tg_username = Column(String, nullable=True)
    tg_token = Column(String, unique=True, nullable=True)
    password = Column(String)
