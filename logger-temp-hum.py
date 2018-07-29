#!/usr/bin/python
import sys, MySQLdb, Adafruit_DHT, datetime, time

# We need to use Adafruit_DHT.DHT22
# And I have the sensor on pin 2
pin = 2
sensor = Adafruit_DHT.DHT22
db = MySQLdb.connect(host='localhost',user='dht22', passwd='dht22pass', db='DHT22')

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
if humidity is not None and temperature is not None:
    cur = db.cursor()
    cur.execute("INSERT INTO InformationTempHum(date, temperature, humidity) VALUES ('" + dt + "'," + str(temperature) + "," + str(humidity) + ")")
    db.commit()
