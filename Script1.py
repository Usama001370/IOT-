from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
from signal import pause
from Adafruit_IO import MQTTClient
import subprocess
import sys, os 

ADAFRUIT_IO_USERNAME = "USERNAME"
ADAFRUIT_IO_KEY = "KEY"

def connected(client):
    client.subscribe('ifttt')

global sleep
global pir
global camera
pir = MotionSensor(4)
camera = PiCamera()
data = {}

#start the camera
camera.rotation = 180
camera.start_preview()

#image image names
i = 0

#Other Methods
#take photo when motion is detected
def take_photo():
    global i
    i = i + 1
    camera.capture('/home/pi/Desktop/image_%s.jpg' % i)
    print('A photo has been taken')
    sleep(10)

#assign a function that runs when motion is detected
pir.when_motion = take_photo

def message(client, feed_id, payload):
    if payload == "4":
       subprocess.call("./ScriptDown", shell=True)
    else:
       print "Unable to KILL the PROCESS PLEASE REFER SYSTEM LOGS"
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

#CALL BACK

client.on_connect = connected
client.on_message = message

client.connect()

client.loop_blocking()
