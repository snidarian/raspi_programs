#!/usr/bin/bash


# First you need to install raspi-config or use raspi-config
# enable the i2c interface in raspi-config
# sudo raspi-config


# run the following script on your pi
curl http://cdn.pisugar.com/release/Pisugar-power-manager.sh | sudo bash


# test if the sugar-pi server is running
echo "get battery" | nc -q 0 127.0.0.1 8423











