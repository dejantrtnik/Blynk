import BlynkLib
import time
from time import sleep
import thread
global blynk
import RPi.GPIO as GPIO

time.sleep(120)

def button_script():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(20,GPIO.OUT)
    GPIO.setup(21,GPIO.OUT)
    GPIO.setup(22, GPIO.IN)
    blynk = BlynkLib.Blynk(xxxxxxxxxxxxxxxxxxxxxx)

    v_array = ['0']
    @blynk.VIRTUAL_WRITE(v_array[0])
    def my_write_handler(value):
        var = (value[0])
        #print(var)
        if var == '1':
            GPIO.output(21,GPIO.HIGH)
            blynk.virtual_write(21,255)
            print("LED on")
        else:
            GPIO.output(21,GPIO.LOW)
            blynk.virtual_write(21,0)
            print("LED off")

    v_array_2 = ['1']  #V1
    @blynk.VIRTUAL_WRITE(v_array_2[0])
    def my_write_handler(value):
        var = (value[0])
        #print(var)
        if var == '1':
            GPIO.output(20,GPIO.HIGH)
            blynk.virtual_write(20,255)
            print("LED on")
        else:
            GPIO.output(20,GPIO.LOW)
            blynk.virtual_write(20,0)
            print("LED off")

    while True:
        try:
            blynk.run()
            if GPIO.input(22) == 1:
                blynk.virtual_write(22,255)
            elif GPIO.input(22) == 0:
                blynk.virtual_write(22,0)
        except:
            internet = "err"
            print("err - neznana napaka")
            time.sleep(1)

            if internet == "napaka":
                button_script()
            elif internet == "int":
                print "Script terminating. Goodbye."

button_script()
