#! /usr/bin/python
# -*- coding:utf-8 -*-
import sys;
import RPi.GPIO as gpio;
import json;
from django.http import HttpResponse;
gpio.setwarnings(False);
gpio.setmode(gpio.BCM);
pin = 17;
args = sys.argv;
ctl = args[1];
if(int(ctl) == 1):
    gpio.setup(pin,gpio.OUT);
    gpio.output(pin,gpio.HIGH);
if(int(ctl) == 0):
    gpio.setup(pin,gpio.OUT);
    gpio.output(pin,gpio.LOW);
