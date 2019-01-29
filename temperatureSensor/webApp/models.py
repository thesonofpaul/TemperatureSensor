from django.db import models

class Account(models.Model):
    account_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    active = models.BooleanField()

class TempSensorHistory(models.Model):
    temperature_f = models.DecimalField()
    humidity = models.DecimalField()
    date_recorded = models.DateField()

class Configuration(models.Model):
    min_temp_threshold = models.DecimalField()
    max_temp_threshold = models.DecimalField()
    email_distrobution = models.CharField()
    sms_distrobution = models.CharField()
    temp_check_interval = models.IntegerField()
