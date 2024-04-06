# This file is meant for loading in cat pics to use in slack.py
import requests

def get_random_cat():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    return response.json()[0]['url']
