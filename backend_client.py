import requests
import api_auth

class Yelp_Client:

    def __init__(self, lat, lon):
        self.api_key = api_auth.get_api_key()
        self.lat = lat
        self.lon = lon
        self.r_base = "https://api.yelp.com/v3/businesses/search"
        self.headers = {'Authorization': "Bearer " + self.api_key}
        #cache of (k, v) -> (food, restaurants[])
        self.cache_rest = {}
        #cache of (k, v) -> (restaurant, reviews[])
        self.cache_rev = {}

    #takes in list of foods to search Yelp with
    #returns dictionary of (k, v) -> (food, restaurants[])
    def get_restaurants_by_foods(self, foods):
        r = {}
        for food in foods:
            if food not in self.cache_rest:
                self.cache_rest[food] = self.get_restaurant_by_food(food)
            r[food] = self.cache_rest[food]
        return r

    #unit of work helper function for get_restaurants_by_foods
    #takes in a food
    #returns list(5) of restaurant names associated with that food
    def get_restaurant_by_food(self, food):
        params = {"term": food, "latitude": self.lat, "longitude": self.lon, "limit": 5}
        response = requests.get(url=self.r_base, params=params, headers=self.headers)
        return [jsn["name"] for jsn in response.json()["businesses"]]

    #returns list of reviews(100) of reviews for a restaurant
    def get_reviews_for_restaurant(self, restaurant):
        return

#test
#returns {'burrito': ['Tacos Sinaloa', 'La Mission', 'La Burrita', 'Fresco Mexican Grill', 'Gordito Amigos']}
client = Yelp_Client("37.87", "-122.26")
print(client.get_restaurants_by_foods(["burrito"]))
