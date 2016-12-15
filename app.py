#!/usr/bin/env python

import urllib
import requests
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
    
    result = req.get("result")
    parameters = result.get("parameters")
    length = parameters.get("number")
    

    print("Request:")
    print(json.dumps(req, indent=4))
    
  
    #url = "https://public-api.adsbexchange.com/VirtualRadar/AircraftList.json?lat=-33.818961&lng=151.105809&fDstL=0&fDstU=1"
    #respons = urllib.urlopen(url)
    #planeData = json.loads(respons.read())
    

    
    #reqq = urllib.urlopen('https://public-api.adsbexchange.com/VirtualRadar/AircraftList.json?lat=-33.818961&lng=151.105809&fDstL=0&fDstU=10')
    
    #readdata = reqq.read()
    
    #planedata = json.loads('{"src":1,"feeds":[{"id":1,"name":"From Consolidator","polarPlot":false}],"srcFeed":1,"showSil":true,"showFlg":true,"showPic":true,"flgH":20,"flgW":85,"acList":[{"Id":8147724,"Rcvr":1,"HasSig":true,"Sig":221,"Icao":"7C530C","Bad":false,"Reg":"VH-QOU","FSeen":"\/Date(1481743979131)\/","TSecs":2488,"CMsgs":1336,"Alt":1575,"GAlt":1634,"InHg":29.9789581,"AltT":0,"TAlt":288,"Call":"QLK220D","Lat":-33.869934,"Long":151.167783,"PosTime":1481746465291,"Mlat":false,"Tisb":false,"Spd":139.1,"Trak":168.0,"TrkH":false,"TTrk":148.359375,"Type":"DH8D","Mdl":"Bombardier DHC-8 402","Man":"Bombardier","CNum":"4275","From":"YSWG Wagga Wagga City, Australia","To":"YSSY Sydney Kingsford Smith, Australia","Op":"QANTAS Link","OpIcao":"SSQ","Sqk":"3747","Help":false,"Vsi":-448,"VsiT":1,"Dst":8.06,"Brng":134.7,"WTC":2,"Species":1,"Engines":"2","EngType":2,"EngMount":0,"Mil":false,"Cou":"Australia","HasPic":false,"Interested":false,"FlightsCount":0,"Gnd":false,"SpdTyp":0,"CallSus":false,"Trt":5,"Year":"2009"},{"Id":7865411,"Rcvr":1,"HasSig":true,"Sig":179,"Icao":"780443","Bad":false,"Reg":"B-6116","FSeen":"\/Date(1481743568723)\/","TSecs":2899,"CMsgs":1243,"Alt":2925,"GAlt":2975,"InHg":29.9704723,"AltT":0,"Call":"CHH7993","Lat":-33.743225,"Long":151.123389,"PosTime":1481746465276,"Mlat":false,"Tisb":false,"Spd":200.4,"Trak":167.9,"TrkH":false,"Type":"A332","Mdl":"Airbus A330 243","Man":"Airbus","CNum":"875","From":"ZLXY Xi'an Xianyang, China","To":"YSSY Sydney Kingsford Smith, Australia","Op":"Hainan Airlines","OpIcao":"CHH","Sqk":"4022","Help":false,"Vsi":64,"VsiT":0,"Dst":8.58,"Brng":10.9,"WTC":3,"Species":1,"Engines":"2","EngType":3,"EngMount":0,"Mil":false,"Cou":"China","HasPic":false,"Interested":false,"FlightsCount":0,"Gnd":false,"SpdTyp":0,"CallSus":false,"Trt":2,"Year":"2007"},{"Id":8153920,"Rcvr":1,"HasSig":true,"Sig":201,"Icao":"7C6B40","Bad":false,"Reg":"VH-VGY","FSeen":"\/Date(1481741947408)\/","TSecs":4520,"CMsgs":1798,"Alt":1100,"GAlt":1062,"InHg":29.88189,"AltT":0,"Call":"JST602","Lat":-33.871874,"Long":151.156654,"PosTime":1481746465291,"Mlat":false,"Tisb":false,"Spd":124.0,"Trak":167.4,"TrkH":false,"Type":"A320","Mdl":"Airbus A320 232","Man":"Airbus","CNum":"4177","From":"YMAV Avalon, Melbourne, Australia","To":"YSSY Sydney Kingsford Smith, Australia","Op":"Jetstar Airways","OpIcao":"JST","Sqk":"3742","Help":false,"Vsi":-768,"VsiT":0,"Dst":7.53,"Brng":141.4,"WTC":2,"Species":1,"Engines":"2","EngType":3,"EngMount":0,"Mil":false,"Cou":"Australia","HasPic":false,"Interested":false,"FlightsCount":0,"Gnd":false,"SpdTyp":0,"CallSus":false,"Trt":2,"Year":"2009"}],"totalAc":7014,"lastDv":"636172813508017927","shtTrlSec":65,"stm":1481746467666}')
    #planedata = json.loads(readdata)
    
    #sampletext = planedata["totalAc"]
    
    # Prepare the data
    query_args = { 'q':'query string', 'foo':'bar' }

    # This urlencodes your data (that's why we need to import urllib at the top)
    data_args = urllib.urlencode(query_args)

    # Send HTTP POST request
    #request_args = urllib2.Request('http://public-api.adsbexchange.com/VirtualRadar/AircraftList.json')
    #resp = urllib2.urlopen(req)
    #request_args = urllib2.Request('https://public-api.adsbexchange.com/VirtualRadar/AircraftList.json')
    
    payload = {'lat': '-33.818961', 'lng': '151.105809', 'fDstL': '0', 'fDstU': length}
    r = requests.get('https://public-api.adsbexchange.com/VirtualRadar/AircraftList.json?', params=payload)
    planedata = json.loads(r.text)
    speech = "";
    if len(planedata["acList"]):
        
        low = planedata["acList"][0]["Dst"]
        place = 0
        for x in range(0, len(planedata["acList"])):
            if planedata["acList"][x]["Dst"] < low:
                place = x
            
            
            
        speech = "There are " + str(len(planedata["acList"])) + " aircraft within " + str(length) + "km. The closest is " + "kilometers away, " + str(planedata["acList"][place]["Op"]) + " flight from " + str(planedata["acList"][place]["From"]) + " to " + str(planedata["acList"][place]["To"]) + ". It's a " + str(planedata["acList"][place]["Man"]) + " " + str(planedata["acList"][place]["Type"])# + ". It's a " + str(planedata["acList"][place]["Man"]# + " " + str(planedata["acList"][place]["Type"]
    else:
        speech = "No planes are nearby"
    
        #str(planedata["acList"][0]["Op"]) + " flight from " + str(planedata["acList"][0]["From"]) + 
       # " to " + str(planedata["acList"][0]["To"]) + "."
    #speech = "There are " + str(planedata["totalAc"])) + " aircraft within 20km"
    res = {
        "speech": speech,
        "displayText": speech,
        
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
