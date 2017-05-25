# tests fix of gh-14 for "from" parameter in the "transfer" function. 
# Proposed convention is to use "_from" as the parameter
# so as not to conflict with "from" Python reserved word.

# _from arg works
# _from arg works with straight json

# Invoke by calling up app access number

# Sample application using the itty-bitty python web framework from:
#  http://github.com/toastdriven/itty

import sys
sys.path = ['..'] + sys.path
from itty import *
from tropo import Tropo, Session, On

TO_NUMBER = 'sip:frank@172.16.22.128:5678'
FROM_NUMBER = 'sip:xiangjun_yu@192.168.26.1:5678'


@post('/index.json')
def index(request):
    t = Tropo()
    #t.say ("One moment please.")
    t.call("sip:xiangjun_yu@192.168.26.1:5678", say = "ha ha ha ha ha ah ah ah ah")
    t.say("ah ah ah ah ah uh uh uh uh ha ha ha")
    on = On("connect", say = "emily", next = "http://freewavesamples.com/files/Kawai-K5000W-AddSquare-C4.wav", post = "http://192.168.26.88:8080/FileUpload/receiveJson").json
    print on
    print '-----------------------' 
    t.transfer(TO_NUMBER, _from= FROM_NUMBER, on=on)
    t.say("Hi. I am a robot")
    json = t.RenderJson()
    print json
    return json


run_itty(config='sample_conf')

