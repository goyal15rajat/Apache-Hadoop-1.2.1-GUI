#!/usr/bin/python
import commands,os
choice = commands.getstatusoutput("zenity --list --title='choose ur mode of choice'  --column='MODE'  Manual  Automatic  Exit")
rchoice=choice[1].split("\n")[1]

if rchoice == 'Manual':
	execfile("man.py")
	'''DEVELOPED BY-RAJAT'''
elif rchoice == 'Automatic' :
	execfile("automatic.py")
else :
	os.system("exit")
