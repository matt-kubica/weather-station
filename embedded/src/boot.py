# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)

import uos, machine

import gc
gc.collect()

import network
from time import sleep

# to configure
WLAN_MODE = network.AP_IF
ESSID = 'ESP8266'
SSID = 'iPhone (Mateusz)'
PASS = 'ojciecdyrektor'

print('WLAN configured to {0}'.format(WLAN_MODE))
wlan = network.WLAN(WLAN_MODE)
wlan.active(True)

if WLAN_MODE == network.STA_IF:
	wlan.connect(SSID, PASS)
	print('\n\n\n\nConnecting to {0}...'.format(SSID), end='')
	while wlan.isconnected() == False:
		print('...', end='')
		sleep(1)
	print('successful!')

elif WLAN_MODE == network.AP_IF:
	wlan.config(essid=ESSID, authmode=network.AUTH_WPA_WPA2_PSK, password=PASS)
	print('\n\n\n\nSetting up access point...', end='')
	while wlan.active() == False:
		print('...', end='')
		sleep(1)
	print('successful!')
