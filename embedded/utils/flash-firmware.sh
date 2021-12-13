#!/bin/bash

export $(xargs < ../../.env.dev)

pipenv run esptool.py --port $ESP_PORT \
	--baud $ESP_BAUD write_flash \
	--flash_size=detect \
	--verify 0 micropython.bin