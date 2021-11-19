import os
import urllib.request
from time import sleep
import random
import numpy as np
import joblib
from dotenv import load_dotenv
load_dotenv()

myurl1 = os.environ.get("URL1")
myurl2 = os.environ.get("URL2")
myurl3 = os.environ.get("URL3")


def randomFunction():
    speed = random.uniform(0 ,3)
    level = random.uniform(-1, 1)
    voltage = random.uniform(100, 260)
    temperature = random.randrange(25, 90)

    return [temperature, level, speed, voltage]


def checkEmergency(speed, temperature):

    governor = 0
    emergency = 0
    
    if speed > 1.8:
        governor = 1
    if temperature > 82:
       emergency = 1

    return [governor, emergency]


def checkHealth(temperature, speed, voltage):
    loaded_model = joblib.load('final_model.sav')
    val = np.array([temperature, speed, voltage])
    res = loaded_model.predict(val.reshape(1, -1))
    if (res == 1.0):
        return "Healthy"
    
    return "Unhealthy"



while True:
    temperature, level, speed, voltage = randomFunction()
    governor, emergency = checkEmergency(speed, temperature)
    print("Condition of elevator 1 : ", checkHealth(float(temperature), speed, voltage))

    urllib.request.urlopen(myurl1 + "&field1=" + str(temperature) + "&field2=" + str(level) + "&field3=" + str(speed) + "&field4=" + str(governor) + "&field5=" + str(voltage) + "&field6=" + str(emergency))

    sleep(1)
    temperature, level, speed, voltage = randomFunction()
    governor, emergency = checkEmergency(speed, temperature)
    print("Condition of elevator 2 : ", checkHealth(float(temperature), speed, voltage))

    urllib.request.urlopen(myurl2 + "&field1=" + str(temperature) + "&field2=" + str(level) + "&field3=" + str(speed) + "&field4=" + str(governor) + "&field5=" + str(voltage) + "&field6=" + str(emergency))

    sleep(1)
    temperature, level, speed, voltage = randomFunction()
    governor, emergency = checkEmergency(speed, temperature)
    print("Condition of elevator 3 : ", checkHealth(float(temperature), speed, voltage))

    urllib.request.urlopen(myurl3 + "&field1=" + str(temperature) + "&field2=" + str(level) + "&field3=" + str(speed) + "&field4=" + str(governor) + "&field5=" + str(voltage) + "&field6=" + str(emergency))

    print("Uploaded")