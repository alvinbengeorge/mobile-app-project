from fastapi import APIRouter
from typing import List
from utilities.response import Response
from utilities.models import Item
from utilities.database import Database
from bson import ObjectId

router = APIRouter()
db = Database()

@router.post("/items")
async def add_items(items: List[Item]):    
    db.db["items"].insert_many([item.dict() for item in items])
    return Response({
        "data": [item.dict() for item in items],
        "message": "Items added successfully"
    })

@router.get("/items")
async def get_items():
    items = list(db.db["items"].find())
    for i in range(len(items)):
        items[i]["_id"] = str(items[i]["_id"])
    return Response({
        "data": items,
        "message": "Items fetched successfully"
    })

@router.delete("/items/{item_id}")
async def delete_item(item_id: str):
    db.db["items"].delete_one({"_id": ObjectId(item_id)})
    return Response({
        "message": "Item deleted successfully"
    })