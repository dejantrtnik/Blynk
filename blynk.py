import os
import glob
import time
import BlynkLib

import Adafruit_BMP.BMP085 as BMP085

sensor = BMP085.BMP085()

BLYNK_AUTH = 'token_key'
blynk = BlynkLib.Blynk(BLYNK_AUTH)
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temp_sensor = '/sys/bus/w1/devices/28-0417511010ff/w1_slave'   # vpišite lastno številko senzorja - v mojem primeru je  "28-0417511010ff"

def read_temp_raw():
    f = open(temp_sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        pressure = float(sensor.read_pressure())/100 + 40
        print(temp_c,'C')
        print(pressure,'hPa')

while True:
        read_temp()
        blynk.virtual_write(2, format(sensor.read_temperature()))
        blynk.virtual_write(3, '{0:0.1f}'.format(float(sensor.read_pressure())/100 +40))
	time.sleep(3)
