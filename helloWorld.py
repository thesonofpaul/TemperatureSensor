#!/usr/bin/python3
import sys
import Adafruit_DHT
import mysql.connector

temperature_f, humidity
successful_reading = False
while not successful_reading:
	humidity, temperature_c = Adafruit_DHT.read_retry(11, 4)
	
	if humidity is not None and temperature_c is not None:
		temperature_f = 9.0/5.0 * temperature_c + 32
		print("Temp: {0:0.1f} F  Humidity: {1:0.1f} %".format(temperature_f, humidity))
		successful_reading = True

cnx = mysql.connector.connect(user='zach_local', password='z4ch333666',
                              host='192.168.1.9')



cnx.close()
