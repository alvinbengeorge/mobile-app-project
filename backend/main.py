from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utilities.response import Response
from utilities.database import Database
from routes import admin

app = FastAPI()
db = Database()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(admin.router, prefix="/admin")

@app.get("/")
async def read_root():
    return Response({"Hello": "World"})