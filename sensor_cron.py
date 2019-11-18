#!/usr/bin/python3
import sys
import datetime
import Adafruit_DHT
from repository import Repository
from sensor import Sensor

if __name__ == '__main__':
    db_file = r"/home/pi/Projects/TemperatureSensor/db/tempSensor.db"
    print("Reading temperature...")
    sensor = Sensor()
    temperature_f, humidity = sensor.read_sensor()
    print("Reading completed.")
    repo = Repository(db_file)
    repo.insert_temperature_record(temperature_f, humidity)
    print ("Inserted record into database.")
