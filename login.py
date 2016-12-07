#!/usr/bin/python
'''                      .
                         .\   / _\   .
                        /_ \   ||   / _
                         ||    ||    ||
                  ; ,     \`.__||__.'/
          |\     /( ;\_.;  `./|  __.'
          ' `.  _|_\/_;-'_ .' '||
           \ _/`       `.-\_ / ||      _
       , _ _`; ,--.   ,--. ;'_ _|,     |
       '`''\| /  ,-\ | _,-\ |/''`'  _  |
        \ .-- \__\_/ /` )_/ --. /   |  |       _
        /    .         -'  .    \ --|--|--.  .' \
       |     /             \     |  |  |   \ |---'
    .   .  -' `-..____...-' `-  .   |  |    |\  _
 .'`'.__ `._      `-..-''    _.'|   |  | _  | `-'      _
  \ .--.`.  `-..__    _,..-'   L|   |    |             |
   '    \ \      _,| |,_      /_7)  |    |   _       _ |  _
         \ \    /       \ _.-'/||        | .' \     _| |  |
          \ \  /.'|   |`.__.'` ||     .--| |--- _   /| |  |
           \ `//_/     \       ||    /   | \  _ \  / | |  |
            `/ \|       |      ||   |    |  `-'  \/  | '--|      _
             `"`'.  _  .'      ||    `--'|                |   .--/
                  \ | /        ||                         '--'
                   |'|         'J        made me do it! ;)
                .-.|||.-.
               '----"----' 
'''
import commands
from sqlcon import *


class Userdetails():

	def setuname(self):
		log = commands.getstatusoutput("zenity --password --username --title='LOGIN DETAILS'")
		print ("\n\n")
		print(log)
		self.uname,upass = (log[1].split("\n"))[1].split("|")

	
		global username
		username=self.uname		

		s=Sqlmethods()
		status =s.Login(username,upass)
		if status == "accepted" :
			execfile("mode.py")
		else :
			os.system("zenity --error --text='Could not fild valid username.\n\tTRY AGAIN'")
			execfile("intro.py")

		

	def	getuname(self):
		global username
		return(username)