#!/usr/bin/env python

import urllib.request
from urllib.error import HTTPError
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))
    
  
    #url = "https://public-api.adsbexchange.com/VirtualRadar/AircraftList.json?lat=-33.818961&lng=151.105809&fDstL=0&fDstU=1"
    #response = urllib.urlopen(url)
    #planeData = json.loads(response.read())
    
    #req = urllib2.Request('https://public-api.adsbexchange.com/VirtualRadar/AircraftList.json?lat=-33.818961&lng=151.105809&fDstL=0&fDstU=1')
    #respoe = urllib2.urlopen(req)
    #the_page = response4.read()
    
    try:

    #url_address ='https://public-api.adsbexchange.com/VirtualRadar/AircraftList.json?lat=-33.818961&lng=151.105809&fDstL=0&fDstU=1'
    #with urllib.request.urlopen(url_address) as url:
        #data = json.loads(url.read())
        #print(data)

    except HTTPError as ex:
        #print(ex.read())
    
    

    res = {
        "speech": "Hello 10",
        "displayText": "yes I'm here too",
        # "data": data,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r



if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=False, port=port, host='0.0.0.0')
