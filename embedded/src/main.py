# imports from upython standard library
from machine import I2C
from time import sleep
import ujson as json
import usocket as socket

# imports from internal modules
from boot import wlan, SERVER_PORT, SDA_PIN, SCL_PIN
from bme import BME280
# creation of bme object - high level wrapper for i2c communication with BME280 sensor
# on ESP8266 pin mappings are following SCL -> GPIO5 (D1), SDA -> GPIO4(D2)
i2c = I2C(scl=SCL_PIN, sda=SDA_PIN, freq=10000)
bme = BME280(i2c=i2c)

# socket creation and port binding
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', SERVER_PORT))
s.listen(5)

print('--- ESP8266 Micropython Wheather Station on {0}:{1} ---'.format(wlan.ifconfig()[0], SERVER_PORT))
while True:
	# blocking call - waiting for external connection
	conn, addr = s.accept()
	request = conn.recv(1024)
	print('Got a request from {0}'.format(addr))

	# creation of json object
	data = {
	  'temperature': bme.temperature,
	  'humidity': bme.humidity,
	  'pressure': bme.pressure
  	}

	# logging to REPL
	print('-- DATA -------------------------------------------------')
	print('\tTemperature: {0}'.format(data['temperature']))
	print('\tHumidity: {0}'.format(data['humidity']))
	print('\tPressure: {0}'.format(data['pressure']))
	print('\n')

	# sending response back
	conn.send('HTTP/1.1 200 OK\n')
	conn.send('Content-Type: application/json\n')
	conn.send('Connection: close\n\n')
	conn.sendall(json.dumps(data))
	conn.close()
