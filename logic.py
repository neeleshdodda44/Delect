import backend_client
import string

get_reviews_for_rest(rest):

latitude = ""
longitude = ""

client = backend_client.Yelp_Client(latitude, longitude)

food_list = shirleys_list

food_to_restaurants = client.get_restaurants(food_list) #dict{food:[restaurants]}

restaurant_results = []
for food in food_to_restaurants.keys():
	restaurants_with_food = food_to_restaurants[food] #[restaurants] corresponding to food
	for restaurant in restaurants_with_food: #restaurant in [restaurants]
		found_restaurant = False
		restaurant_review_list = client.get_reviews_for_restaurant(restaurant) #[reviews] for restaurant
		#strip punctuation and split review into words set --> review_set
		for review in restaurant_review_list:
			review_string = review
			exclude = set(string.punctuation)
			review_string = ''.join(ch for ch in review_string if ch not in exclude)
			#print(review_string)
			review_split = review_string.split(" ")
			review_set = set(review_split)
			if review_set.contains(food):
				restaurant_results.append(restaurant)
				found_restaurant = True
				break #stop looking at reviews for this restaurant
		if found_restaurant:
			continue
return restaurant_results

# import string
#
# review_string = "hello! how are you doing today? isn't it such a great day today"
# exclude = set(string.punctuation)
# review_string = ''.join(ch for ch in review_string if ch not in exclude)
# print(review_string)
