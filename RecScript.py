import subprocess
import sys, os
from Adafruit_IO import MQTTClient

ADAFRUIT_IO_USERNAME = "Username" 
ADAFRUIT_IO_KEY = "ADA Fruit AIO KEY"

def connected(client):
    client.subscribe('ifttt')

def message(client, feed_id, payload):
     if payload == "1":
       execfile('Script1.py')
       #subprocess.call("./Script1.py", shell=True)
     elif payload == "2":
       subprocess.call("./RPCam", shell=True) 
     elif payload == "3":
       subprocess.call("./RPCamStop", shell=True)
     elif payload == "4":
       subprocess.call("./ScriptDown", shell=True)
     else:
        print "Message from IFTTT: %s" % payload

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_message    = message

client.connect()

client.loop_blocking() # block forever on client loop
