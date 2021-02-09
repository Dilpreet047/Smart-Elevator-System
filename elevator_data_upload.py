import sys
import urllib.request
from time import sleep
import random

myurl = "Thingspeak URL"

while True:
    speed = random.uniform(0 ,3)
    governor = 0
    level = random.uniform(-1, 1)
    voltage = random.uniform(100, 260)
    temperature = random.randrange(25, 90)
    emergency = 0

    if speed > 1.8:
        governor += 1
    if temperature > 82:
        emergency = 1
    urllib.request.urlopen(myurl + "fields")


#In this way we sent the data to the Thingspeak IoT platform.