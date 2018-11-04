#!/bin/bash

END=`date --date="2019-01-28 11:07:10" +"%s"` 


for ((i = 0; i < 1000; i++))
do
    python monitor.py >> log.txt 
done
