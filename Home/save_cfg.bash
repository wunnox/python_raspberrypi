#!/bin/bash
##############################################
#
# Name: save_cfg.bash
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 04.04.2016 - V1.0
#
# Purpose: Sichert Konfig Files
#
##############################################

savedire="/data"
dom=`date +%d`

for i in /opt/fhem/fhem.cfg
do
  name=`basename $i`
  namesave="$name.$dom"
  cp $i /data/$namesave
done
