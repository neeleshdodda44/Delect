import requests
import api_auth
import json
import collections

class Yelp_Client:

    def __init__(self, lat, lon):
        self.api_key = api_auth.get_api_key()
        self.lat = lat
        self.lon = lon
        self.search_base = "https://api.yelp.com/v3/businesses/search"
        self.reviews_base = "https://api.yelp.com/v3/businesses/"
        self.headers = {'Authorization': "Bearer " + self.api_key}
        #cache of (k, v) -> (food, (restaurant, id)[])
        self.cache_rest = {}

        #cache of (k, v) -> (business id, review[])
        self.reviews = collections.defaultdict(list)
        with open("dataset.json") as f:
            for line in f:
                data = json.loads(line)
                self.reviews[data["business_id"]].append(data["text"])


    #returns dictionary of (k, v) -> (food, (restaurant, id)[])
    def get_restaurants_by_foods(self, foods):
        r = {}
        for food in foods:
            if food not in self.cache_rest:
                self.cache_rest[food] = self.get_restaurant_by_food(food)
            r[food] = self.cache_rest[food]
        return r

    #returns (restaurant, id)[5] associated with that food
    def get_restaurant_by_food(self, food):
        params = {"term": food, "latitude": self.lat, "longitude": self.lon, "limit": 30}
        response = requests.get(url=self.search_base, params=params, headers=self.headers)
        return [(jsn["name"], jsn["id"]) for jsn in response.json()["businesses"]]

    #returns review[100] for a restaurant
    def get_reviews_for_restaurant(self, id):
        if len(self.reviews) > 100:
            return self.reviews[id][:100]

        return self.reviews[id]

#test
#returns {'burrito': ['Tacos Sinaloa', 'La Mission', 'La Burrita', 'Fresco Mexican Grill', 'Gordito Amigos']}
# client = Yelp_Client("37.87", "-122.26")
# print(client.get_reviews_for_restaurant('q33FT8iYvU2UUbJuiEQWUw'))
