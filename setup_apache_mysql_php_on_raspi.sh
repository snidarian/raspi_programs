#!/usr/bin/bash
# This script installs and sets up Apache, mysql and php on a raspi pi 3 namely



# Update and upgrade the current system
sudo apt update && sudo apt upgrade


echo "updating system..."


# Install Apache
echo "Installing apache2"
sudo apt install apache2

# installing apache will create a folder called 'www' in the /var/ directory. In that folder it creates a directory names 'html'. We need to now give our 'pi' user ownership of those directories because they are created with root ownership originally.


echo "changing ownership and permissions of /var/www/html/ folder"
# Recursively (for the whole folder) change ownership to user 'pi' and group 'www-data'
sudo chown -R pi:www-data /var/www/html/

# change rwx permissions for the '/var/www/html/' folder
# add rwx for user and group (www-data)
sudo chmod -R 770 /var/www/html/


# now its time to check if apache is working.

# should be able to reach it on 127.0.0.1 at port 80 (default apache server port)
# you can also reach the server by putting in the ip address of the raspberry pi device or
# you can also reach the server by putting in the hostname of the raspberry pi


echo "Check if the apache server is working by visiting 127.0.0.1 (port 80)..."
sleep 3


# CONTROLLING THE APACHE2 DAEMON

# start
# sudo apache2ctl start
# stop
# sudo apache2ctl stop
# restart
# sudo apache2ctl restart
# check status
# systemctl status apache2 


echo "Press Enter to continue..."
read continuevar


# ------------------------------------------------------------
# INSTALLING PHP ONTO THE RASPI

sudo apt install php php-mbstring


# to check if php is working:

# To know if PHP is working properly the method is the same to the one used for Apache.
# but first delete the file “index.html” in the directory “/var/www/html”.
# sudo rm /var/www/html/index.html
# Then create an “index.php” file in this directory, with this command line
# echo "<?php phpinfo ();?>" > /var/www/html/index.php

# then visit 127.0.0.1 the same way you did before to see the php infopage


# if you want to keep hold of the index.html file without creating problems,
# rename it to index.html.unavailable




# ---------------------------------------------------------------------
# INSTALLING MYSQL SERVER


sudo apt install mariadb-server php-mysql


# verify that MySQL is working correctly

# sudo mysql --user=root


# Installing PHPMyAdmin
# This is not essential but is a security measure

sudo apt install phpmyadmin

# PHPMyAdmin installation program will ask you few question. About the dbconfig-common part, choose to not use it (as we have already configure our database). About the server to configure PHPMyAdmin for, choose Apache. And the root password is the one you set for MySQL.


# You should also enable mysqli extension

# install php-mysqli
sudo apt-get install php-mysqli

# DONT CONFIGURE MYSQL through phpmyadmin. Just configure root password for mysql with the program itself.


# check that PHPMyAdmin is working properly
# http://127.0.0.1/phpadmin

# if it's not working create a symbolic link between /usr/share/phpmyadmin and /var/www/html/phpmyadmin
sudo ln -s /usr/share/phpmyadmin /var/www/html/phpmyadmin

# Now visit 127.0.0.1/phpmyadmin and login as the root MySQL user!

# Now you have a GUI remote access interface to your MySQL server.

# Create databases, tables, write SQL queries all like you normally would with MySQL command, BUT if you want/need to use a GUI to interact with database information and control systems, you can.



# this was originally sourced from https://howtoraspberrypi.com/how-to-install-web-server-raspberry-pi-lamp/


