#!/usr/bin/python
import os,commands
from sqlcon import *
from login import *


class Saveip(Intro):
	
	global username
	def __init__(self):
		global username
		u=Userdetails()
		username=u.getuname()

	def savenode(self,nnaddress,ddaddress,jtaddress,ttaddress):
		global username
		rnnip=' '.join(nnaddress)
		rddip=' '.join(ddaddress)
		rjtip=' '.join(jtaddress)
		rttip=' '.join(ttaddress)
				
		stmt.execute("INSERT INTO IP(NAME,NNIP,DDIP,TTIP,JTIP) VALUES(\'"+username+"\',\'"+rnnip+"\',\'"+rddip+"\',\'"+rttip+"\',\'"+rjtip+"\');")
		conn.commit()
						
	def takenode(self):
		global username
		stmt.execute("SELECT * FROM IP;")
		results=stmt.fetchall()
		namearr=[]
		nnarr=[]
		ddarr=[]
		jtarr=[]
		ttarr=[]
		
		for row in results:
			namearr.append(row[0])
			nnarr.append(row[1])
			ddarr.append(row[2])
			ttarr.append(row[3])
			jtarr.append(row[4])

		x = namearr.index(username)
		
		nn=nnarr[x]
		dd=ddarr[x]
		tt=ttarr[x]
		jt=jtarr[x]

		print("nn is  " +nn)
		print("dd is  " +dd)
		print("tt is  " +tt)
		print("jt is  " +jt)

		return(nn,dd,tt,jt)	

	def checknode(self):
			global username
			stmt.execute("SELECT * FROM IP;")
			results=stmt.fetchall()
			namearr=[]
			nnarr=[]
			ddarr=[]
			jtarr=[]
			ttarr=[]
			
			for row in results:
				namearr.append(row[0])
				nnarr.append(row[1])
				ddarr.append(row[2])
				ttarr.append(row[3])
				jtarr.append(row[4])

			if username in namearr:
				return("present")
			else :
				return("no")


									
	