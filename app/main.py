import json

import uvicorn
from fastapi import FastAPI
from app.routes import users, status
from app.models.user import User

app = FastAPI()
app.include_router(users.router)
app.include_router(status.router)
users: list[User]


if __name__ == "__main__":

    with open("users.json") as f:
        users = json.load(f)

    for user in users:
        User.model_validate(user)

    uvicorn.run(app, host="localhost", port=8002)
