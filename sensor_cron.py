#!/usr/bin/python3
import sys
import datetime
import Adafruit_DHT
from repository import Repository

def read_sensor():
    temperature_f = -100
    humidity = -100
    successful_reading = False
    while not successful_reading:
        humidity, temperature_c = Adafruit_DHT.read_retry(11, 4)
        if humidity is not None and temperature_c is not None:
            temperature_f = 9.0/5.0 * temperature_c + 32
            print("Temp: {0:0.1f} F  Humidity: {1:0.1f} %".format(temperature_f, humidity))
            successful_reading = True
    return temperature_f, humidity

if __name__ == '__main__':
    db_file = r"/home/zip822/Projects/TemperatureSensor/db/tempSensor.db"
    
    temperature_f, humidity = read_sensor()
    
    repo = Repository(db_file)
    repo.insert_temperature_record(temperature_f, humidity)
