import json
from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from MongoDBclient import restaurant_collection
app = FastAPI()

restaruants = {
 [restaurant_collection]




}


@app.get("/getRestaurant/{restaurant_id}")
def get_Restaurants(restaurant_id: int = Path(..., title="The ID of the restaurant you want to view", ge=1, le=1)):
    return restaruants[restaurant_id]

@app.get("/getRestaurants")
def get_Restaurants():
    restaurants = list(restaruants.find({}))
    return restaurants



@app.get("/get-by-menu")
def get_by_menu(menu: Optional[str] = Query(..., title="The menu item you want to search for", min_length=3)):
    return {item_id: restaruants[item_id] for item_id in restaruants if restaruants[item_id]["menu"] == menu}


@app.get("/get-by-city/{item_id}")
def get_by_city(*, item_id: int, city: Optional[str] = Query(..., title="The city you want to search for", min_length=3)):
    try:
        return {item_id: restaruants[item_id] for item_id in restaruants if restaruants[item_id]["city"] == city}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
