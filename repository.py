#!/usr/bin/python3
import sys
from datetime import datetime  
from datetime import timedelta  
import sqlite3
from sqlite3 import Error
from setting import Setting
from account import Account

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
    
    def get_settings(self):
        """ retrieve min and max temperature settings """
        get_settings_sql = ''' SELECT * FROM setting '''
        try:
            conn = self.create_connection()
            with conn:
                c = conn.cursor()
                c.execute(get_settings_sql)
                ret_val = c.fetchall()
                print(ret_val)
                return self._format_settings(ret_val)                
        except Error as e:
            print(e)

    def _format_settings(self, ret_val):
        min_temp = 0.
        max_temp = 100.
        for val in ret_val:
            if val[0] == "minTemp":
                min_temp = float(val[1])
            elif val[0] == "maxTemp":
                max_temp = float(val[1])
            else:
                print("unknown value: {}, {}".format(val[0], val[1]))
        return Setting(min_temp, max_temp)
    
    def get_accounts_active_sms(self):
        """ retrieve sms on sms-enabled accounts """
        get_active_sms_sql = '''
            SELECT firstName, lastName, emailAddress, sms
            FROM account
            WHERE enableSms = 1
            '''
        try:
            conn = self.create_connection()
            with conn:
                c = conn.cursor()
                c.execute(get_active_sms_sql)
                ret_val = c.fetchall()
                print(ret_val)
                return self._format_accounts(ret_val)
        except Error as e:
            print(e)

    def get_accounts_active_email(self):
        """ retrieve email addresses on email-enabled accounts """
        get_active_email_sql = '''
            SELECT firstName, lastName, emailAddress, sms
            FROM account
            WHERE enableEmail = 1
            '''
        try:
            conn = self.create_connection()
            with conn:
                c = conn.cursor()
                c.execute(get_active_email_sql)
                ret_val = c.fetchall()
                print(ret_val)
                return self._format_accounts(ret_val)
        except Error as e:
            print(e)

    def _format_accounts(self, ret_val):
        account_list = []
        for val in ret_val:
            if len(val) < 4:
                print("bad data: {}".format(val))
            account_list.append(Account(val[0], val[1], val[2], val[3]))
        return account_list

if __name__ == '__main__':
    db_file = r"C:/Users/zip82/Projects/TemperatureSensor/db/tempSensor.db"
    try:
        repo = Repository(db_file)
        # repo.get_settings()
        repo.get_accounts_active_email()
    except Error as e:
        print(e)
