#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################################
#
# Name: pushmeldung.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 31.07.2015 - V1.0
#
# Purpose: Versendet eine Pushmeldung
#
##############################################

import subprocess

subprocess.call(['curl', '-s', '-F', 'token=afQxD9NrGTiwoH4iJJ1RHjXJViHZyU', '-F', 'user=uWNgPiQLx9LqoK4WwNPj7zba6otBWL', '-F', 'message=Web-Seite Offline', 'https://api.pushover.net/1/messages.json'])
