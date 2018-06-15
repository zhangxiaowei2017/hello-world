#! /usr/bin/python
# -*- coding:utf-8 -*-
import sys;
import RPi.GPIO as gpio;
import json;
from django.http import HttpResponse;
gpio.setwarnings(False);
gpio.setmode(gpio.BCM);
def startJidianqi(request):
    pin = 17;
    str = "";
    commond = request.GET['commond'];
    if(commond == "1" or commond == "0"):
        if(int(commond) == 1):
            gpio.setup(pin,gpio.OUT);
            gpio.output(pin,gpio.HIGH);
            str = "正在开始浇水";
        if(int(commond) == 0):
            gpio.setup(pin,gpio.OUT);
            gpio.output(pin,gpio.LOW);
            str = "已经停止浇水"
    else:
        str = "命令有错误，请重新操作";
    msg = {"msg":str};
    return HttpResponse(json.dumps(msg),content_type="application/json");
