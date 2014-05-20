### SecurePi
### Frank Olson
### V.1
### 20 May 2014
### Python 2.7.5
### Last Update: 20 May 2014

### Raspberry Pi Security System which will use a hiden switch to arm and disarm
### the system. The Pi will monitor door, window, and motion sensors and when
### input is detected a picture from the webcam is emailed to my personal email
### notifying me of an intruder

# Import Libraries
import RPr.GPIO as GPIO
import subprocess
import datetime
import time
import os

# Pin Mode Setup
GPIO.setmode(GPIO.BCM)

# Pin Setup
doorPin = 
