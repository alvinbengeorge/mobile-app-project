from fastapi import APIRouter
from typing import List
from utilities.response import Response
from utilities.models import Item
from utilities.database import Database

router = APIRouter()
db = Database()

@router.post("/items")
async def add_items(items: List[Item]):    
    db.db["items"].insert_many([item.dict() for item in items])
    return Response({
        "data": items,
        "message": "Items added successfully"
    })