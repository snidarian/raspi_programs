#!/usr/bin/bash


while [ 1 ];
do
    echo -e "\n\n\n\n"
    echo "#########################"
    vcgencmd measure_temp
    vcgencmd measure_clock arm
    echo "#########################"
    sleep 1
    clear
done
