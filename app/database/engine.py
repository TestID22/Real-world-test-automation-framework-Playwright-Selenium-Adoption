import os

from sqlmodel import SQLModel, text
from sqlalchemy.orm import Session
from app.models.user import User
from sqlalchemy import create_engine


engine = create_engine(os.getenv("DATABASE_ENGINE"))
users_db: list[User] = []


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def check_availability():
    try:
        with Session(engine) as session:
            session.execute(text("SELECT 1"))
        return True
    except Exception as e:
        print(e)
        return False
