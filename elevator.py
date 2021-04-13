import sys
import urllib.request
from time import sleep
import random

myurl = "https://api.thingspeak.com/update?api_key=5NKLBPLHTEJC42RI"

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
    urllib.request.urlopen(myurl + "&field1=" + str(temperature) + "&field2=" + str(level) + "&field3=" + str(speed) + "&field4=" + str(governor) + "&field5=" + str(voltage) + "&field6=" + str(emergency))
    print("Uploaded")