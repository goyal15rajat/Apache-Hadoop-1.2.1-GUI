#!/usr/bin/python
import os,commands,MySQLdb,sqlcon

class Sqlmethods(Intro):

	def Signup(self,uname,upass):
		
		print(uname)
		print(upass)
		stmt.execute("INSERT INTO LOGIN(NAME,PASS) VALUES(\'"+uname+"\',\'"+upass+"\');")
		conn.commit()