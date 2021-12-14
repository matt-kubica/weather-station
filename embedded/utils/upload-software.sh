#!/bin/bash

export $(xargs < ../../.env.dev)

echo "Uploading software to $ESP_PORT using ampy..." && \

for file in ../src/*.py
do
    echo "Uploading $file"
    pipenv run ampy --port $ESP_PORT --baud $ESP_BAUD put $file
done && \
echo "Software uploaded, restart your ESP and access it on $ESP_PORT with $ESP_BAUD baud rate" || \
echo "Software upload failed..."