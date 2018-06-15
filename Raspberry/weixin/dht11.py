#!/usr/bin/python
#coding:utf-8
import sys
import RPi.GPIO as gpio
import Adafruit_DHT
import time
import datetime
import json
from django.http import HttpResponse
sensor = Adafruit_DHT.DHT11
def getDht11Data(request):
    pin = 4
    humidity,temperature = Adafruit_DHT.read_retry(sensor,pin)
    if humidity is not None and temperature is not None:
        data = {'temperature':temperature,'humidity':str(humidity) + "%",'time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))}
        print("data",data);
        return HttpResponse(json.dumps(data),"application/json");
    else:
        print('read data is failuer,please try again!')
        return HttpResponse("无法读取数据","text/plain")
