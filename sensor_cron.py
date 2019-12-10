#!/usr/bin/python3
from repository import Repository
# from sensor import Sensor
from email_manager import Email

def read_temperature(is_test):
    print("Reading temperature...")
    if is_test:
        return 69.6, 96.9
    # else:
    #     sensor = Sensor()
    #     temperature_f, humidity = sensor.read_sensor()
    #     return temperature_f, humidity

def insert_record(repo, temperature_f, humidity):
    print("Inserting record into database.")
    repo.insert_temperature_record(temperature_f, humidity)

def should_alert(repo, settings, temperature_f):
    return temperature_f >= settings.max_temp or temperature_f <= settings.min_temp

if __name__ == '__main__':
    db_file = r"C:/Users/zip82/Projects/TemperatureSensor/db/tempSensor.db"
    repo = Repository(db_file)
    
    settings = repo.get_settings()
    temperature_f, humidity = read_temperature(True)
    insert_record(repo, temperature_f, humidity)
    print(temperature_f, settings.min_temp, settings.max_temp)
    if should_alert(repo, settings, temperature_f):
        print("Alerting...")
        email = Email()
        email_accounts = repo.get_accounts_active_email()
        print(email_accounts)
        email.send_alert(email_accounts, temperature_f, settings)

