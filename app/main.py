import json
import uvicorn
from fastapi import FastAPI

from app.routes import users, status
from app.models.user import User
from app.database import users_db

app = FastAPI()
app.include_router(users.router)
app.include_router(status.router)


if __name__ == "__main__":

    with open("users.json") as f:
        users_db.extend(json.load(f))

    for user in users_db:
        User.model_validate(user)

    uvicorn.run(app, host="localhost", port=8002)
