#!/usr/bin/python
# importing the requests library
# coding=utf-8
import requests
import sys
import json
import argparse


movie_name = sys.argv[1]
apikey = "BanMePlz"
#YEAR = "1969"

# defining a params dict for the parameters to be sent to the API
#PARAMS = {'t':movie_name,"apikey":apikey,"y":YEAR}
PARAMS = {'t':movie_name,"apikey":apikey}

# api-endpoint
URL = "http://omdbapi.com/"

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

# extracting data in json format
data = r.json()
ini_string = json.dumps(data)
decoded = json.loads(ini_string)

rotten_tomatoes = decoded['Ratings'][1]["Source"]
rotten_tomatoes_rating = decoded['Ratings'][1]["Value"]

print('{0} : {1}'.format(rotten_tomatoes,rotten_tomatoes_rating))
