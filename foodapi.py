import json
import logging
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson import json_util
from typing import List
import uvicorn 
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import motor.motor_asyncio as motor 
import os 

app = FastAPI()

# Add CORS middleware to allow requests from other domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Update with your app's domain or '*' to allow all domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = None

class RestaurantModel:
    db_name = "Foodiez"
    collection_name = "Restaurants"

    @staticmethod
    async def get_all_restaurants() -> List[dict]:
        db = client[RestaurantModel.db_name]
        collection = db[RestaurantModel.collection_name]
        cursor = collection.find({})
        restaurants = list(await cursor.to_list(length=None))
        return restaurants

@app.on_event("startup")
async def startup_event():
    global client
    mongo_uri = os.environ.get("mongodb://localhost:27017/")
    client = AsyncIOMotorClient(mongo_uri)

@app.on_event("shutdown")
async def shutdown_event():
    global client
    client.close()

@app.get("/getRestaurant")  # Changed from /getRestaurants to /getRestaurant
async def get_restaurants() -> List[dict]:
    try:
        restaurants = await RestaurantModel.get_all_restaurants()
        if not restaurants:
            raise HTTPException(status_code=204, detail="No restaurants found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

    # Convert the response to a JSON-serializable format
    response = json.loads(json_util.dumps(restaurants))
    return {
        "status": "success",
        "data": response,
        "Access-Control-Allow-Origin": "*", # Update with your app's domain or '*' to allow all domains
    }
