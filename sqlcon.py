#!/usr/bin/python
import os,commands,MySQLdb



class Intro():
	def __init__(self):
		global conn
		conn  = MySQLdb.connect('localhost','root','root')
		global stmt
		stmt = conn.cursor()
		stmt.execute("USE PRO ;")
		stmt.execute("CREATE TABLE IF NOT EXISTS LOGIN(NAME VARCHAR(20) NOT NULL,PASS VARCHAR(40) NOT NULL,PRIMARY KEY(NAME)) ;")
		stmt.execute("CREATE TABLE IF NOT EXISTS IP(NAME VARCHAR(20),NNIP VARCHAR(30),DDIP VARCHAR(200),TTIP VARCHAR(200),JTIP VARCHAR(30),PRIMARY KEY(NAME)) ;")
		
class Sqlmethods(Intro):

	def Signup(self,uname,upass):
		
		print(uname)
		print(upass)
		stmt.execute("INSERT INTO LOGIN(NAME,PASS) VALUES(\'"+uname+"\',\'"+upass+"\');")
		conn.commit()		

	def  Login(self,uname,upass):
		
		print(uname)
		print(upass)
		stmt.execute("SELECT * FROM LOGIN;")
		results = stmt.fetchall()
		namearr= []
		passwrdarr=[]

		for row in results:
			namearr.append(row[0])
			passwrdarr.append(row[1])
			'''DEVELOPED BY-RAJAT'''

		if uname in namearr:
			x = namearr.index(uname)
		else :
			return("illegal")

		if passwrdarr[x] == upass:
			return("accepted")
		else :
			return("illegal")		

	


