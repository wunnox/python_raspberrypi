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
# Purpose: Misst die Temperatur und Luftfeuchtigkeit
#
##############################################

#Module
import adafruit_dht
import board

def sensor_dht22():
    '''dht2302 Temperatur/Feuchtigkeitssensor'''

    # GPIO Pin angeben

    try:
        dhtDevice = adafruit_dht.DHT22(board.D17)
        #Messungen einlesen
        temp_aussen = dhtDevice.temperature
        humid_aussen = dhtDevice.humidity
        return temp_aussen,humid_aussen

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        return 0.0,0.0

if __name__=='__main__':
   temp_aussen,humid_aussen=sensor_dht22()
   print("Temperatur  : {:.1f} % ".format(temp_aussen))
   print("Feuchtigkeit: {} % ".format(humid_aussen))
