import uvicorn
from fastapi import FastAPI


app = FastAPI()

@app.get("/api/user")
def get_user():
    return {"user": "test user"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8002)
