#!/usr/bin/python
# importing the requests library
# coding=utf-8
import requests
import sys
import json
import argparse
import const

def main():
    movie_name = sys.argv[1]
    apikey = sys.argv[2]

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'t':movie_name,"apikey":apikey}
    rotten_tomatoes_rating = getRatings(PARAMS)
    print('{0} : {1}'.format('rotten tomatoes ratings',rotten_tomatoes_rating))

def getRatings(PARAMS):
    # sending get request and saving the response as response object
    r = requests.get(url = const.OMDBAPI_URL, params = PARAMS)
    
    # extracting data in json format
    data = r.json()
    ini_string = json.dumps(data)
    decoded = json.loads(ini_string)

    rotten_tomatoes = decoded['Ratings'][1]["Source"]
    rotten_tomatoes_rating = decoded['Ratings'][1]["Value"]
    return rotten_tomatoes_rating

  
if __name__== "__main__":
  main()