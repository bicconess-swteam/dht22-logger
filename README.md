
# Temperature and Humidity 🌡️

This is a Python Script for logging the humidity and the temperature on a Date Base (MySQL/MariaDB) from a DHT22 sensor.

## Requirements
* *DHT22 sensor* -> https://www.sparkfun.com/datasheets/Sensors/Temperature/DHT22.pdf
* *Raspberry PI*
* *Adafruit Python DHT Sensor Library* -> https://github.com/adafruit/Adafruit_Python_DHT
* *MariaDB/MySQL*

## Instalation

For this project we need to have the Adafruit library installed on our raspberry.

Create a new user on our SQL Database.
```sql
CREATE USER 'username'@'localhost' IDENTIFIED BY 'pass';
```
Create a new database.
```sql
CREATE DATABASE DHT22;
```
Permissions to our user for that database.
```sql
GRANT ALL PRIVILEGES ON *.* TO ‘username’@‘localhost’;
```
Create a new table where we save this information.
```sql
CREATE TABLE Reading (
    id INT AUTO_INCREMENT NOT NULL,
	date DATETIME NOT NULL,
	temperature DECIMAL(5,2) NOT NULL,
	humidity DECIMAL(5,2) NOT NULL,
	PRIMARY KEY (id)
	);
```

Now, if we execute the script, we have in our database the information of humidity and temperature, but...What happens if we want this to be done automatically?
***We could use the crontab file to automate this process!!!😎😎***
```sh
crontab -e
```
And in this file we want to create a new line with our service. For example:
```txt
*/5 * * * *  /home/pi/Development/dht22-logger/logger-temp-hum.py &> /dev/null
```
