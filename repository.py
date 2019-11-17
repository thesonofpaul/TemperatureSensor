#!/usr/bin/python3
import sys
from datetime import datetime  
from datetime import timedelta  
import sqlite3
from sqlite3 import Error

class Repository:

    def __init__(self, db_file):
        self.db_file = db_file

    def create_connection(self):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except Error as e:
            print(e)

    def insert_temperature_record(self, temperature, humidity):
        """ insert a record into temperature table """
        create_table_sql = ''' INSERT INTO temperature(temperature,humidity,date_recorded) VALUES(?,?,?) '''
        try:
            date_recorded = datetime.now()
            params = (temperature, humidity, date_recorded)
            conn = self.create_connection()
            with conn:
                c = conn.cursor()
                c.execute(create_table_sql, params)
        except Error as e:
            print(e)

    def clear_temperature_records(self):
        """ clear records over a month old """
        clear_old_records_sql = ''' DELETE * FROM temperature WHERE date_recorded < ? '''
        try:
            date_threshold = datetime.now() - timedelta(days=30)
            params = (date_threshold)
            conn = self.create_connection()
            with conn:
                c = conn.cursor()
                c.execute(clear_old_records_sql, params)
        except Error as e:
            print(e)

# if __name__ == '__main__':
#     db_file = r"/home/zip822/Projects/TemperatureSensor/db/tempSensor.db"
#     try:
#         repo = Repository(db_file)
#         repo.insert_temperature_record(69.6, 96.9)
#     except Error as e:
#         print(e)
