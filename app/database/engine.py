import os

from sqlmodel import SQLModel

from app.models.user import User
from sqlalchemy import create_engine


engine = create_engine(os.getenv("DATABASE_ENGINE"), pool_size=10)
users_db: list[User] = []


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
