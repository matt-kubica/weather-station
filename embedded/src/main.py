from time import sleep
import ujson as json
import usocket as socket

from boot import station
from machine import Pin, I2C
from bme import BME280
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)
bme = BME280(i2c=i2c)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

print('--- ESP8266 Micropython Wheather Station on {0} ---'.format(station.ifconfig()[0]))
while True:
	conn, addr = s.accept()
	request = conn.recv(1024)
	print('Got a request from {0}'.format(addr))

	data = {
	  'temperature': bme.temperature,
	  'humidity': bme.humidity,
	  'pressure': bme.pressure
  	}

	print('-- DATA -----------------------------------')
	print('\tTemperature: {0}'.format(data['temperature']))
	print('\tHumidity: {0}'.format(data['humidity']))
	print('\tPressure: {0}'.format(data['pressure']))
	print('\n')

	conn.send('HTTP/1.1 200 OK\n')
	conn.send('Content-Type: application/json\n')
	conn.send('Connection: close\n\n')
	conn.sendall(json.dumps(data))
	conn.close()
