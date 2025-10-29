from http import HTTPStatus
from fastapi import HTTPException, APIRouter

from app.database import users_db
from app.models.user import User

users_db: list[User]
router = APIRouter()

@router.get("/api/users/{user_id}", status_code=HTTPStatus.OK)
def get_user(user_id: int) -> User:
    if user_id <= 0:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="User_id is invalid")
    if user_id >= len(users_db):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    return users_db[user_id]

@router.get("/api/users")
def get_users() -> list[User]:
    return users_db
