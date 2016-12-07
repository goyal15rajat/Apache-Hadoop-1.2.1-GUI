#!/usr/bin/python
import commands


log = commands.getstatusoutput("zenity --password --username --title='LOGIN DETAILS'") 
print ("\n\n")
print(log)

uname,upass = (log[1].split("\n"))[1].split("|")
s=Sqlmethods()
s.Signup(uname,upass)
execfile("intro.py")
