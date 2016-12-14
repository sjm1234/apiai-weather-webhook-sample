#!/usr/bin/env python

import urllib
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
    #respons = urllib.urlopen(url)
    #planeData = json.loads(respons.read())
    

    
    reqq = urllib.urlopen('https://public-api.adsbexchange.com/VirtualRadar/AircraftList.json?lat=-33.818961&lng=151.105809&fDstL=0&fDstU=1')
   
    readdata = reqq.read()
    
    planedata = json.loads('{"src":1,"feeds":[{"id":1,"name":"From Consolidator","polarPlot":false}],"srcFeed":1,"showSil":true,"showFlg":true,"showPic":true,"flgH":20,"flgW":85,"acList":[],"totalAc":3292,"lastDv":"636172813226560026","shtTrlSec":65,"stm":1481692022571}')
    #planedataa = json.loads(readdata)
    
    sampletext = planedata['src']
        

    res = {
        "speech": "Ted" + " 3",
        "displayText": "yes I'm here too",
        
        #"data": [simon: "yes"],
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
