#!/usr/bin/bash
# This script installs and sets up Apache, mysql and php on a raspi pi 3 namely



# Update and upgrade the current system
sudo apt update && sudo apt upgrade



# Install Apache
sudo apt install apache2


# Recursively (for the whole folder) change ownership to user 'pi' and group 'www-data'
sudo chown -R pi:www-data /var/www/html/

# change rwx permissions for the '/var/www/html/' folder
sudo chmod -R 770 /var/www/html/



# now its time to check if apache is working.

# should be able to reach it on 127.0.0.1 at port 80 (default apache server port)





























