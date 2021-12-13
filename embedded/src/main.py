

HEADER_LINE = '--- ESP8266 Micropython Wheather Station on {0} ---'

print('Micropython initialized')
while True:
	inet_address = station.ifconfig()[0]
	populated_header = HEADER_LINE.format(inet_address)

	print(populated_header)
	print('\tTemperature: {0}'.format(bme.temperature))
	print('\tHumidity: {0}'.format(bme.humidity))
	print('\tPressure: {0}'.format(bme.pressure))
	print('-' * len(populated_header))

	sleep(5)