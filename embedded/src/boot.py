# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)

import uos, machine

import gc
gc.collect()

from machine import Pin, I2C
from bme import BME280
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)
bme = BME280(i2c=i2c)

import network
from time import sleep
SSID = 'Genesis'
PASS = 'ojciecdyrektor'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(SSID, PASS)

print('\n\n\n\n')
print('Connecting to {0}...'.format(SSID), end='')
while station.isconnected() == False:
	print('...', end='')
	sleep(1)
print('successful!')