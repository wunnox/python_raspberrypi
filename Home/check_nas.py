#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################################
#
# Name: check_nas.py
#
# Author: Peter Christen
#
# Version: 1.1
# 
# Date: 15.09.2015 - V1.0
#       31.07.2016 - V1.1: Pushmeldung hinzugefügt
#
# Purpose: Prüft ob beide NAS laufen
#
##############################################

import os, datetime, subprocess

#Variabeln
now = datetime.datetime.now()
datum=now.strftime("%d.%m.%Y %H:%M")
nas1="NAS1 ist nicht verfügbar!!"
nas2="NAS2 ist nicht verfügbar!!"
nas="NAS ok"

if os.system("ping -c 1 192.168.1.80") == 0:
    nas1="NAS1 ist erreichbar\n"
    print "NAS1 ist erreichbar"
else:
    print "NAS1 ist NICHT erreichbar"
    nas="NAS hat Probleme"
    subprocess.call(['curl', '-s', '-F', 'token=afQxD9NrGTiwoH4iJJ1RHjXJViHZyU', '-F', 'user=uWNgPiQLx9LqoK4WwNPj7zba6otBWL', '-F', 'message=NAS1 nicht erreichbar', 'https://api.pushover.net/1/messages.json'])

if os.system("ping -c 1 192.168.1.82") == 0:
    nas2="NAS2 ist erreichbar\n"
    print "NAS2 ist erreichbar"
else:
    print "NAS2 ist NICHT erreichbar"
    nas="NAS hat Probleme"
    subprocess.call(['curl', '-s', '-F', 'token=afQxD9NrGTiwoH4iJJ1RHjXJViHZyU', '-F', 'user=uWNgPiQLx9LqoK4WwNPj7zba6otBWL', '-F', 'message=NAS2 nicht erreichbar', 'https://api.pushover.net/1/messages.json'])

me=nas+" :/tmp/check_nas.log"
f=open('/tmp/send_nas.log', 'w')
f.write(me)
f.close()

f=open('/tmp/check_nas.log', 'w')
header="### NAS Check vom "+datum+" ###\n"
f.write(header)
f.write(nas1)
f.write(nas2)
f.close()
