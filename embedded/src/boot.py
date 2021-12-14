# this file is executed on every boot (including wake-boot from deepsleep)

# default imports
import esp, uos, machine, gc
esp.osdebug(None)
gc.collect()

# networking setup
import network
from time import sleep

# those constants determine how wlan should be configured
# - in case of STATION mode (STA_IF) board connects to external access point - SSID and PASS hold credentials of this external access point
# - in case of ACCESS POINT mode (AP_IF) other stations can connect to board - SSID and PASS holds credentials to provide when connecting
WLAN_MODE = network.STA_IF # or AP_IF
SSID = 'some-ssid'
PASS = 'some-pass'

# other constants
SERVER_PORT = 80
SDA_PIN = machine.Pin(4)
SCL_PIN = machine.Pin(5)

print('WLAN configured to {0}'.format(WLAN_MODE))
wlan = network.WLAN(WLAN_MODE)
wlan.active(True)

# depending on mode differen actions are performed
if WLAN_MODE == network.STA_IF:
	wlan.connect(SSID, PASS)
	print('\n\n\n\nConnecting to {0}...'.format(SSID), end='')
	while wlan.isconnected() == False:
		print('...', end='')
		sleep(1)
	print('successful!')

elif WLAN_MODE == network.AP_IF:
	wlan.config(essid=SSID, authmode=network.AUTH_WPA_WPA2_PSK, password=PASS)
	print('\n\n\n\nSetting up access point...', end='')
	while wlan.active() == False:
		print('...', end='')
		sleep(1)
	print('successful!')
