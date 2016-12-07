#!/usr/bin/python
import commands,os
from hmenu import *
h=Had()

while(True):
	choice=commands.getstatusoutput("zenity --list --title='choose ur mode of choice'  --column='ACTION'  Upload  Delete  MR View  Exit")[1].split('\n')[1]

	if choice == 'Upload':
		print(choice)
		filename=h.up("file")
		h.hdfsupload(filename)
	elif choice == 'Delete':
		print(choice)
		h.filedelete()
	elif choice == 'MR':
		print(choice)	
		h.mrrun()
	elif choice == 'View':
		print(choice)
		h.view()
	else:
		break
		os.system('exit')
		print(choice)			