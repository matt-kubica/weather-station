#!/bin/bash

export $(xargs < ../../.env.dev)

pipenv run esptool.py --port $ESP_PORT \
		   --baud $ESP_BAUD erase_flash  