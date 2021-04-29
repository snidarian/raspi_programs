#!/usr/bin/bash
# This script installs and sets up Apache, mysql and php on a raspi pi 3 namely



# Update and upgrade the current system
sudo apt update && sudo apt upgrade



# Install Apache
sudo apt install apache2

# installing apache will create a folder called 'www' in the /var/ directory. In that folder it creates a directory names 'html'. We need to now give our 'pi' user ownership of those directories because they are created with root ownership originally.


# Recursively (for the whole folder) change ownership to user 'pi' and group 'www-data'
sudo chown -R pi:www-data /var/www/html/

# change rwx permissions for the '/var/www/html/' folder
# add rwx for user and group (www-data)
sudo chmod -R 770 /var/www/html/



# now its time to check if apache is working.

# should be able to reach it on 127.0.0.1 at port 80 (default apache server port)





























