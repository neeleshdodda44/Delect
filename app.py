from flask import Flask, render_template, request, redirect, url_for, Response, json
import requests
import pandas as pd
from collections import defaultdict

application = Flask(__name__)
application.config['DEBUG'] = True

@application.route("/", methods=['GET', 'POST'])
def main():
    return 'Hello World'

@application.route("/places", methods=['GET', 'POST'])
def places():
    assert foods in request.form, "Argument 'foods' not passed!"
    foods = request.form['foods'].split(',')
    restaurants = None 
    # do some call here to get final list of restaurants returned
    assert isinstance(restaurants, list), 'Returned item is not list!'
    return restaurants
    # return render_template('name_of_html_here) # name of file to be returned.

if __name__ == "__main__":
    application.run()
