from typing import Optional
from pydantic import BaseModel
class Restaurant(BaseModel):
    id: int
    Restaurantname: str
    Restaurantlocation: str
    Restaurantrating: int
    Restaurantdescription: str
    restaurantstype_id: str
    Restaurantphone: Optional[str] = None
    DeepLinkURL: str
    Restaurantlatitude: int
    Restaurantlongitude: int 

