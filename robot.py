from flask import Flask
from flask import Flask, render_template, request
import RPi.GPIO as GPIO
from gpiozero import MotionSensor

import time


app = Flask(__name__)

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

m11=5

m12=6

m21=20

m22=21

e1=13

e2=12


GPIO.setup(m11, GPIO.OUT)

GPIO.setup(m12, GPIO.OUT)

GPIO.setup(m21, GPIO.OUT)

GPIO.setup(m22, GPIO.OUT)

GPIO.setup(e1, GPIO.OUT)

GPIO.setup(e2, GPIO.OUT)

GPIO.output(m11 , 0)

GPIO.output(m12 , 0)

GPIO.output(m21, 0)

GPIO.output(m22, 0)

GPIO.output(e1, 1)

GPIO.output(e2, 1)

print ("Done")

@app.route("/")

def index():
	
	return render_template('robot.html',**templateData)

@app.route('/left_side')

def left_side():

    data1="LEFT"

    GPIO.output(m11 , 1)

    GPIO.output(m12 , 0)

    GPIO.output(m21 , 0)

    GPIO.output(m22 , 0)

    return 'true'


@app.route('/right_side')

def right_side():

   data1="RIGHT"

   GPIO.output(m11 , 0)

   GPIO.output(m12 , 0)

   GPIO.output(m21 , 0)

   GPIO.output(m22 , 1)

   return 'true'


@app.route('/up_side')

def up_side():

   data1="FORWARD"

   GPIO.output(m11 , 1)

   GPIO.output(m12 , 0)

   GPIO.output(m21 , 0)

   GPIO.output(m22 , 1)

   return 'true'


@app.route('/down_side')

def down_side():

   data1="BACK"

   GPIO.output(m11 , 0)

   GPIO.output(m12 , 1)

   GPIO.output(m21 , 1)

   GPIO.output(m22 , 0)

   return 'true'


@app.route('/stop')

def stop():

   data1="STOP"

   GPIO.output(m11 , 0)

   GPIO.output(m12 , 0)

   GPIO.output(m21 , 0)

   GPIO.output(m22 , 0)

   return  'true'


if __name__ == "__main__":

 print ("Start")

 app.run(host='0.0.0.0',port=5000,debug=True)
