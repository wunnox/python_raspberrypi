#!/usr/bin/python3
# -*- coding: utf-8 -*-
##############################################
#
# Name: fhem_analyse.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 05.12.2016 - V1.0
#
# Purpose: Daten aus fhem-Log-Dateien einlesen
#
##############################################

import sqlite3,os,sys,datetime,subprocess

#Variabeln
logpfad="/opt/fhem/log"
mydatabase="/data/fhem.db"
connection=sqlite3.connect(mydatabase)
cursor=connection.cursor()
now = datetime.datetime.now()
heute=now.strftime("%Y/%m/%d")
jetzt=now.strftime("%H:%M")
an=0
co=0
alarm=0

#DB erstellen
cursor.execute('create table if not exists fhem ( Nr varchar(20) primary key, Datum date, Zeit time, Target varchar(30), Trigger varchar(10))')
cursor.execute('create index if not exists fhem_ind on fhem (Datum)')
cursor.execute('create table if not exists aktuell ( Target varchar(30) primary key, Datum date, Zeit time, Trigger varchar(10))')

#Eingabe prüfen
l=len(sys.argv)
for w in range(1, l):
    if '-a' in sys.argv[w]:
        an=1
        #analyse=sys.argv[w+1]
    if '-c' in sys.argv[w]:
        co=1
    if '-A' in sys.argv[w]:
        alarm=1
    if '-?' in sys.argv[w]:
        print ("Usage: fhem_analyse.py [-c | -a]")
        print (" ")
        print ("Options:")
        print (" -c : Collect data")
        print (" -a <Target> : Analyse data for <Target>")

if co==1:
  for file in os.listdir(logpfad):
   if "Fenster" in file or "Tuere" in file:
      print ("Lese File", file)

      logfile=logpfad+"/"+file
      f=open(logfile, 'r')
      allezeilen = f.readlines()
      f.close()

      z=0
      zo=0
      for zeile in allezeilen:
         z+=1
         datumzeit=zeile[:19]
         ind=datumzeit.replace('-','').replace('_','').replace(':','')
         datum,zeit=datumzeit.split('_')
         datum=datum.replace('-','/')
         ind=ind+str(z)
         w=zeile.split(' ')
         target=w[1]
         trigger=w[2].replace('\n','')
         if "closed" in w[2] or "open" in w[2]:
            zo+=1
            #print (ind, datum, zeit, target, trigger)
            cursor.execute("insert or ignore into fhem values(?,?,?,?,?)",(ind,datum,zeit,target,trigger))
      connection.commit()
      print (z,"Zeilen eingelesen,", zo, "geschreiben")

  #Aktueller Status erfassen
  
if an==1:
   target_l=[]
   cursor.execute('delete from aktuell')   
   cursor.execute('select distinct Target from fhem')   
   for row in cursor:
      target_l.append(row[0])

   for t in target_l:
      cursor.execute('replace into aktuell select Target,Datum,max(Zeit),Trigger from fhem where Datum=? and Target=?',(heute,t))   

   connection.commit()
      
   target_l=[]
   cursor.execute("select Target from aktuell where Trigger='open'")   
   for row in cursor:
      target_l.append(row[0])

   Target=''
   if len(target_l)>0:
      for t in target_l:
         Target=Target+t+", "

      message="Folgende Target sind offen: "+Target[:-2]
      print (message)
      meldung="subprocess.call(['curl', '-s', '-F', 'token=afQxD9NrGTiwoH4iJJ1RHjXJViHZyU', '-F', 'user=uWNgPiQLx9LqoK4WwNPj7zba6otBWL', '-F', 'message="+message+"', 'https://api.pushover.net/1/messages.json'])"
      if alarm==1:
         exec(meldung)

cursor.close()

