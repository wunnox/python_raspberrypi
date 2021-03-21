#!/bin/bash
##############################################
#
# Name: save_scripts.bash
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 31.07.2016 - V1.0
#
# Purpose: Sichert das scripts-Verzeichnis
#
##############################################

rsync -a /home/pi/scripts/ /data/scripts
