import json

import uvicorn
from http import HTTPStatus
from fastapi import FastAPI, HTTPException

from framework.models.user import User

app = FastAPI()
users: list[User]


@app.get("/api/users/{user_id}", status_code=HTTPStatus.OK)
def get_user(user_id: int) -> User:
    if user_id >= len(users):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    return users[user_id]

@app.get("/api/users")
def get_users() -> list[User]:
    return users


if __name__ == "__main__":

    with open("users.json") as f:
        users = json.load(f)

    for user in users:
        User.model_validate(user)

    uvicorn.run(app, host="localhost", port=8002)
