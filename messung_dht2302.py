#!/usr/bin/python3
##############################################
#
# Name: messung_dht2302.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 09.12.2020
# Date:
# Date:
#
# Sensor: DHT22/AM2302 Digitaler Temperatur und Feuchtigskeitssensor
# Purpose: Misst die Temperatur und Luftfeuchtigkeit
# Module:
#   - pip3 install adafruit-circuitpython-dht
#   - sudo apt-get install libgpiod2
#
##############################################

#Module
import adafruit_dht
import board

#Variabeln
pin=board.D17 # GPIO Pin angeben

def sensor_dht22():
    '''Messung ausführen'''

    try:
        dhtDevice = adafruit_dht.DHT22(pin)
        #Messungen einlesen
        temp = dhtDevice.temperature
        humid = dhtDevice.humidity
        return temp,humid

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        return 0.0,0.0

if __name__=='__main__':
   temp,humid=sensor_dht22()
   print("Temperatur  : {:.1f} °C ".format(temp))
   print("Feuchtigkeit: {} % ".format(humid))
