#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################################
#
# Name: check_site.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 15.08.2015 - V1.0
#
# Purpose: Prüft verschiedene Webseiten ob diese funktionieren
#
##############################################


import sys, urllib

# Verbindung zu einer URL
u = urllib.urlopen("http://www.savetravelbelt.com/savetravelbelt/Welcome.html")

# Liest alle Zeilen in eine Liste
li = u.readlines()

# Schliesst die Verbindung
u.close()

# Ausgabe der Liste
for element in li:
     print element

