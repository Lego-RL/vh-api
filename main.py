from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class Comment(BaseModel):
    timestamp: int
    message: str


app = FastAPI()
greeting: dict = {"Hello": "World!"}

@app.get("/")
def read_root():
    return greeting

@app.post("/comment")
async def store_comment(comment: Comment):
    """
    Retrieve and store single comment.
    """

    global greeting 
    greeting = comment.dict()

    return comment


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)