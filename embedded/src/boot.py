# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)

import uos, machine

import gc
gc.collect()

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