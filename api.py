#!/usr/bin/python
# importing the requests library
# coding=utf-8
import requests
import sys
import json
import argparse
import const

def main():
    if len(sys.argv) < 3:
        sys.exit('Arguments Missing')
        
    movie_name = sys.argv[1]
    apikey = sys.argv[2]

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'t':movie_name,"apikey":apikey}
    rotten_tomatoes_rating = getRatings(PARAMS)
    #print rotten_tomatoes_rating

    if rotten_tomatoes_rating is not None:
        print('{0} : {1}'.format('rotten tomatoes ratings',rotten_tomatoes_rating))
    else: 
        print('{0}'.format('No such Movie exists or Api Key is incorrect'))

def getRatings(PARAMS):
    # sending get request and saving the response as response object
    decoded = getRequests(const.OMDBAPI_URL, PARAMS)
    
    if "Ratings" in decoded: 
        rotten_tomatoes = decoded['Ratings'][1]["Source"]
        rotten_tomatoes_rating = decoded['Ratings'][1]["Value"]
        return rotten_tomatoes_rating
    else:
        return None

def getRequests(req_url, req_params):
    # sending get request and saving the response as response object
    r = requests.get(url = req_url, params = req_params)
    
    # extracting data in json format
    data = r.json()
    ini_string = json.dumps(data)
    decoded = json.loads(ini_string)
    #print decoded
    return decoded
  
if __name__== "__main__":
  main()