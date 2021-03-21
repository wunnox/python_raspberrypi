#!/bin/bash
##############################################
#
# Name: check_mail.bash
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 15.09.2015 - V1.0
#
# Purpose: Prüft auf Logfiles zum senden
#
##############################################

dire="/tmp"

cd $dire

for i in `ls send_*`
do
 sub=`cat $i | cut -f1 -d ":"`
 file=`cat $i | cut -f2 -d ":"`
 mailx -s "$sub" peter.christen@chp.ch <$file
 rm $i
done
