import backend_client
import string

latitude = "37.87"
longitude = "-122.26"

client = backend_client.Yelp_Client(latitude, longitude)

food_list = ["chicken salad"]

food_to_restaurants = client.get_restaurants_by_foods(food_list) #dict{food:[(restaurant, id)]}

restaurant_results = []

for food in food_to_restaurants.keys():
	#print(food_to_restaurants[food])
	restaurants_with_food = food_to_restaurants[food] #[(restaurant, id)] corresponding to food
	print(food_to_restaurants[food])
	for restaurant, id in restaurants_with_food: #restaurant, id in [(restaurant, id)]
		#found_restaurant = False
		restaurant_review_list = client.get_reviews_for_restaurant(id) #[reviews] for restaurant
		#print(restaurant, food, restaurant_review_list)
		#strip punctuation and split review into words set --> review_set
		for review in restaurant_review_list:
			review_string = review
			exclude = set(string.punctuation)
			review_string = ''.join(ch for ch in review_string if ch not in exclude)
			#print(review_string)
			review_split = review_string.split(" ")
			review_set = set(review_split)
			if food in review_set:
				restaurant_results.append((restaurant, food))
				#found_restaurant = True
				break #stop looking at reviews for this restaurant
		# if found_restaurant:
		# 	continue
print(restaurant_results)

# import string
#
# review_string = "hello! how are you doing today? isn't it such a great day today"
# exclude = set(string.punctuation)
# review_string = ''.join(ch for ch in review_string if ch not in exclude)
# print(review_string)
