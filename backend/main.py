from fastapi import FastAPI
from utilities.response import Response
from utilities.database import Database

app = FastAPI()
db = Database()

@app.get("/")
async def read_root():
    return Response({"Hello": "World"})