#!/usr/bin/python3
import os  
import time  
import datetime  
import glob  
import MySQLdb 
import Adafruit_DHT 
from time import strftime    



#DHT_SENSOR = Adafruit_DHT.DHT11
#DHT_PIN = 4
  
#Variables for MySQL  
db = MySQLdb.connect(host="localhost", user="user", passwd="password", db="sensor") # replace password with your password  
cur = db.cursor()  

while True:

    humidity2, temperature2 = Adafruit_DHT.read_retry(11, 4)

    convert = temperature2 * 1.8 + 32

    #print ('Temp: {0:0.1f} F  Humidity: {1:0.1f} %'.format(convert, humidity))
  
    def dateTime(): #get UNIX time  
            secs = float(time.time())  
            secs = secs*1000  
            return secs  
  
    def tempRead(): #read temperature, return float with 3 decimal places  
            degrees = float('{0:.3f}'.format(convert))  
            return degrees  

    def humidityRead(): #read humidity, return float with 3 decimal places  
            humidity = float('{0:.3f}'.format(humidity2))  
            return humidity  
  
    secs = dateTime()  
    temperature = tempRead()    
    humidity = humidityRead()  
  
    sql = ("""INSERT INTO dhtsensor (datetime,temperature,humidity) VALUES (%s,%s,%s)""", (secs, temperature, humidity))  
  
    try:  
        print ("Writing to the database...")  
        cur.execute(*sql)  
        db.commit()  
        print ("Write complete")  
  
    except:  
        db.rollback()  
        print ("We have a problem")  
  
    cur.close()  
    db.close()  
  
    print (secs)  
    print (temperature)    
    print (humidity)
    exit () 
