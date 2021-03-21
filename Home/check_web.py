#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################################
#
# Name: check_web.py
#
# Author: Peter Christen
#
# Version: 1.1
# 
# Date: 15.08.2015 - V1.0
#       31.07.2016 - V1.1: Pushmeldung eingefügt
#
# Purpose: Prüft verschiedene Webseiten ob diese funktionieren
#
##############################################


import sys, urllib, datetime, subprocess

#Variabeln
w=["http://www.chp.ch/chp/Willkommen.html","http://www.cssgmbh.ch/cssgmbh/Willkommen.html","http://www.zouberhuet.ch","http://www.savetravelbelt.com/savetravelbelt/Welcome.html"]
p=["Familie Christen","Willkommen","Willkommen bei der Kita Zouberhuet","Save travel"]
s=("chp","cssgmbh","zouberhuet","savetravelbelt")
now = datetime.datetime.now()
datum=now.strftime("%d.%m.%Y %H:%M")
fehler=0
check=[]

l=len(w)
for i in range(0,l):
   try:
      # Verbindung zu Seite testen
      u = urllib.urlopen(w[i])

      # Liest alle Zeilen in eine Liste
      li = u.readlines()

      # Schliesst die Verbindung
      u.close()
   except:
      li="Error"

   # Ausgabe der Liste
   mess="Seite "+s[i]+" hat ein Problem"
   check.append(mess)
   e=1
   for element in li:
     #print element
     if p[i] in element:
         e=0
         mess="Seite "+s[i]+" ist ok"
         check[i]=mess

   if e==1:
      fehler=1

if fehler==1:
    print "Fehlerhafte Seite"
    stat="Fehlerhafte Web-Seite"
    subprocess.call(['curl', '-s', '-F', 'token=afQxD9NrGTiwoH4iJJ1RHjXJViHZyU', '-F', 'user=uWNgPiQLx9LqoK4WwNPj7zba6otBWL', '-F', 'message=Web-Seite Offline', 'https://api.pushover.net/1/messages.json'])
else:
    print "Alle Seiten ok"
    stat="Alle Web-Seiten ok"

me=stat+" :/tmp/check_web.log"
f=open('/tmp/send_web.log', 'w')
f.write(me)
f.close()

f=open('/tmp/check_web.log', 'w')
header="### WebSite Check vom "+datum+" ###\n"
f.write(header)
l=len(check)
for i in range(0,l):
   print check[i]
   f.write(check[i])
   f.write("\n")
f.close()

