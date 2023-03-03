
from mongoengine import Document ,IntField, StringField, FloatField
class Restaurants(Document):
    Restaurantname = StringField(required=True)
    Restaurantlocation = StringField(required=True)
    Restaurantrating = FloatField(required=True)
    Restaurantdescription = StringField(required=True)
    restaurantstype_id = StringField(required=True)
    DeepLinkURL = StringField(required=False)
    Restaurantlatitude = FloatField(required=True)
    Restaurantlongitude = FloatField(required=True)
    Restaurantphone = StringField(required=False)
    Restaurantwebsite = StringField(required=False)
    RestaurantImage = StringField(required=True)




