from http import HTTPStatus
from fastapi import HTTPException, APIRouter

from app.database import users
from app.models.user import User

users_db: list[User]
router = APIRouter()

@router.get("/api/users/{user_id}", status_code=HTTPStatus.OK)
def get_user(user_id: int) -> User:
    if user_id < 1:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="User_id is invalid")
    user = users.get_user(user_id)
    if not user:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    return user

@router.get("/api/users")
def get_users() :
    return users.get_users()
