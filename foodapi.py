import json
import logging
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson import json_util
from typing import List
import uvicorn 
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Add CORS middleware to allow requests from other domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Update with your app's domain or '*' to allow all domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RestaurantModel:
    db_name = "Foodiez"
    collection_name = "Restaurants"

    @staticmethod
    async def get_all_restaurants() -> List[dict]:
        client = MongoClient("mongodb://localhost:27017/?directConnection=true")
        db = client[RestaurantModel.db_name]
        collection = db[RestaurantModel.collection_name]
        restaurants = await collection.find({}).to_list(length=None)
        client.close() # close the connection to the MongoDB server after fetching the data
        return restaurants


@app.get("/getRestaurants")
async def get_restaurants() -> List[dict]:
    try:
        restaurants = await RestaurantModel.get_all_restaurants()
        if not restaurants:
            raise HTTPException(status_code=204, detail="No restaurants found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

    # Convert the response to a JSON-serializable format
    # Convert the response to a JSON-serializable format and add CORS headers
    response = json.loads(json_util.dumps(restaurants))
    return {
        "status": "success",
        "data": response,
        "Access-Control-Allow-Origin": "*", # Update with your app's domain or '*' to allow all domains
    }





