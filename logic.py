import backend_client
import string

latitude = "37.87"
longitude = "-122.26"

client = backend_client.Yelp_Client(latitude, longitude)

food_list = ["chicken", "pizza", "salad", "coffee"]

food_to_restaurants = client.get_restaurants_by_foods(food_list) #dict{food:[(restaurant, id)]}

restaurant_results = []
restaurant_results_final = []
restaurant_counts = {}

def find_matches_without_reviews():
	for food in food_to_restaurants.keys():
		#print(food_to_restaurants[food])
		restaurants_with_food = food_to_restaurants[food] #[(restaurant, id)] corresponding to food
		print(food_to_restaurants[food])
		for restaurant, id in restaurants_with_food: #restaurant, id in [(restaurant, id)]
			restaurant_results.append((restaurant, food))
			if restaurant in restaurant_counts:
				restaurant_counts[restaurant] += 1
			else:
				restaurant_counts[restaurant] = 1

	for restaurant, id in restaurant_results:
		if restaurant_counts[restaurant] >= 2:
			restaurant_results_final.append((restaurant, id))
	print(restaurant_results)
	print(restaurant_counts)
	print(restaurant_results_final)

def find_matches_with_reviews():
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
					if restaurant in restaurant_counts:
						restaurant_counts[restaurant] += 1
					else:
						restaurant_counts[restaurant] = 1
					#found_restaurant = True
					break #stop looking at reviews for this restaurant

	for restaurant, id in restaurant_results:
		if restaurant_counts[restaurant] >= 2:
			restaurant_results_final.append((restaurant, id))
	print(restaurant_results)
	print(restaurant_counts)
	print(restaurant_results_final)

#find_matches_without_reviews()
find_matches_with_reviews()
# import string
#
# review_string = "hello! how are you doing today? isn't it such a great day today"
# exclude = set(string.punctuation)
# review_string = ''.join(ch for ch in review_string if ch not in exclude)
# print(review_string)
