#!/usr/bin/python3
import sys
# import Adafruit_DHT
import mysql.connector

# temperature_f, humidity
# successful_reading = False
# while not successful_reading:
# 	humidity, temperature_c = Adafruit_DHT.read_retry(11, 4)
	
# 	if humidity is not None and temperature_c is not None:
# 		temperature_f = 9.0/5.0 * temperature_c + 32
# 		print("Temp: {0:0.1f} F  Humidity: {1:0.1f} %".format(temperature_f, humidity))
# 		successful_reading = True

def add_account(username, password):
	sql = 'INSERT INTO account(username, password, active) VALUES(%(username)s, %(password)s, 1)'
	sql_data = {
		'username': username,
		'password': password
	}
	cursor.execute(sql, sql_data)
	print(cursor.lastrowid)
	cnx.commit()
	return

def get_accounts():
	sql = 'SELECT * FROM account'
	cursor.execute(sql)

	for (id, username, password, active) in cursor:
		print('id: {0}, username: {1}, password: {2}, active: {3}'
			.format(id, username, password, True if active==1 else False))

def sql_test():
	sql = 'SELECT * FROM '

def open_connection():
	try:
		cnx = mysql.connector.connect(
			user='zach_local', 
			password='',
			host='192.168.1.9', 
			database='temperature_sensor',
			auth_plugin='mysql_native_password')
		cursor = cnx.cursor()
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with your user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database does not exist")
		else:
			print(err)
	return cnx, cursor

def close_connection():
	cursor.close()
	cnx.close()
	return

cnx, cursor = open_connection()

# add_account('bingle', 'berry')
get_accounts()

close_connection()
