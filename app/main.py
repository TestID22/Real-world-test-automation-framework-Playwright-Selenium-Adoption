import json
import dotenv
import uvicorn
from fastapi import FastAPI

env = dotenv.load_dotenv()

from app.routes import users, status
from app.models.user import User
from app.database.engine import users_db, create_db_and_tables


app = FastAPI()
app.include_router(users.router)
app.include_router(status.router)


if __name__ == "__main__":
    create_db_and_tables()
    with open("users.json") as f:
        users_db.extend(json.load(f))

    for user in users_db:
        User.model_validate(user)

    uvicorn.run(app, host="localhost", port=8002)
