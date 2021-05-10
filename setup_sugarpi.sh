#!/usr/bin/bash


# First you need to install raspi-config or use raspi-config
# enable the i2c interface in raspi-config
# sudo raspi-config


# run the following script on your pi
curl http://cdn.pisugar.com/release/Pisugar-power-manager.sh | sudo bash


# by default the sugarpi-server is disables so it must be enabled to start serving battery data
sudo systemctl enable pisugar-server
# start the 'pisugar-server' server
sudo systemctl start pisugar-server
# Check the status of the daemon/server with this command
sudo systemctl status pisugar-server
# The server daemon will also respond to 'stop' and 'disable'

# test if the sugar-pi server is running
echo "get battery" | nc -q 0 127.0.0.1 8423











