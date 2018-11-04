from flask import Flask, render_template, request, redirect, url_for, Response, json
import requests
import pandas as pd
from collections import defaultdict
import backend_client
import string
import collections

from logic import find_matches_without_reviews

application = Flask(__name__)
application.config['DEBUG'] = True
backend_client = backend_client.Yelp_Client("37.87", "-122.26")

@application.route("/", methods=['GET', 'POST'])
def main():
    return render_template('index.html')

@application.route("/places", methods=['GET', 'POST'])
def places():
    #assert 'foods' in request.form, "Argument 'foods' not passed!"
    #foods = request.form['foods'].split(',')
    foods = ['burrito', 'apple', 'beef', 'taco']
    restaurants = list(find_matches_without_reviews(foods, 0.5, backend_client).keys())
    print(restaurants)
    # do some call here to get final list of restaurants returned
    assert isinstance(restaurants, list), 'Returned item is not list!'
    restaurants_string = ','.join(restaurants)
    return render_template('response.html', restaurants=restaurants_string)
    # return render_template('name_of_html_here) # name of file to be returned.
    

if __name__ == "__main__":
    application.run()
