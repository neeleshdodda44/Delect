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
    assert 'foods' in request.form, "Argument 'foods' not passed!"
    assert 'threshold' in request.form
    foods = request.form['foods'].split(',')
    threshold = float(request.form['threshold'])
    restaurants_dict = find_matches_without_reviews(foods, threshold, backend_client)
    keys = list(restaurants_dict.keys())
    values = list([', '.join(value) for value in restaurants_dict.values()])
    str_format = "{key}: {value}"
    print(keys)
    print(values)
    combined = ';'.join([str_format.format(key=key, value=value) for key,value in zip(keys,values)])
    return render_template('response.html', restaurants=combined)
    

if __name__ == "__main__":
    application.run()
