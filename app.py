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
    
    planedata = json.loads('{"src":1,"feeds":[{"id":1,"name":"From Consolidator","polarPlot":false}],"srcFeed":1,"showSil":true,"showFlg":true,"showPic":true,"flgH":20,"flgW":85,"acList":[{"Id":8159414,"Rcvr":1,"HasSig":true,"Sig":181,"Icao":"7C80B6","Bad":false,"Reg":"VH-ZPK","FSeen":"\/Date(1481742403862)\/","TSecs":3359,"CMsgs":1525,"Alt":6025,"GAlt":6075,"InHg":29.9704723,"AltT":0,"Call":"VOZ803","Lat":-33.847412,"Long":151.031463,"PosTime":1481745761822,"Mlat":false,"Tisb":false,"Spd":266.7,"Trak":353.5,"TrkH":false,"Type":"E190","Mdl":"Embraer EMB-190 AR","Man":"Embraer","CNum":"19000218","From":"YMML Melbourne, Australia","To":"YSSY Sydney Kingsford Smith, Australia","Op":"Virgin Australia","OpIcao":"VOZ","Sqk":"4044","Help":false,"Vsi":-1792,"VsiT":1,"Dst":7.56,"Brng":245.2,"WTC":2,"Species":1,"Engines":"2","EngType":3,"EngMount":0,"Mil":false,"Cou":"Australia","HasPic":false,"Interested":false,"FlightsCount":0,"Gnd":false,"SpdTyp":0,"CallSus":false,"Trt":4},{"Id":8154554,"Rcvr":1,"HasSig":true,"Sig":203,"Icao":"7C6DBA","Bad":false,"Reg":"VH-VYK","FSeen":"\/Date(1481742337627)\/","TSecs":3425,"CMsgs":1550,"Alt":2925,"GAlt":2975,"InHg":29.9704723,"AltT":0,"Call":"QFA400","Lat":-33.748184,"Long":151.096001,"PosTime":1481745761822,"Mlat":false,"Tisb":false,"Spd":201.3,"Trak":128.7,"TrkH":false,"Type":"B738","Mdl":"Boeing 737NG 838/W","Man":"Boeing","CNum":"34183","From":"YMML Melbourne, Australia","To":"YSSY Sydney Kingsford Smith, Australia","Op":"Qantas","OpIcao":"QFA","Sqk":"4004","Help":false,"Vsi":-64,"VsiT":0,"Dst":7.92,"Brng":353.4,"WTC":2,"Species":1,"Engines":"2","EngType":3,"EngMount":0,"Mil":false,"Cou":"Australia","HasPic":false,"Interested":false,"FlightsCount":0,"Gnd":false,"SpdTyp":0,"CallSus":false,"Trt":2,"Year":"2005"}],"totalAc":7096,"lastDv":"636172813537825615","shtTrlSec":65,"stm":1481745763540}')
    sampletext = planedata["totalAc"]
    speech = "Today in 1" + str(sampletext)

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
