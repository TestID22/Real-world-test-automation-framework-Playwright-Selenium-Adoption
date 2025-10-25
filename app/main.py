from http import HTTPStatus

import uvicorn
from fastapi import FastAPI


app = FastAPI()

@app.get("/api/user", status_code=HTTPStatus.OK)
def get_user():
    return {"user": "test user"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8002)
