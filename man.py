#!/usr/bin/python
import commands,os
from docker import *
from nodes import *
from ipsave import *


def findadd(l,iplist,dockaddress):
	newl=[]
	for i in l:
		n=iplist.index(i)
		m=(dockaddress[n]).split(" ")[1]
		newl.append(m)	
	return(newl)	



s=Saveip()

status=s.checknode()
if status=="present":
	execfile("hadoopmenu.py")
else:
	nsystems=commands.getstatusoutput("zenity --title='Manula details' --entry --text='enter no of systems'")
	systems=int(nsystems[1].split('\n')[1])
	print(systems)
	d=Doc()
	docklist=d.makedoc(systems)
	print(docklist)



	#taking ip
	dockaddress=d.ipdoc(docklist)
	print(dockaddress)

	iplist=[]
	for i in dockaddress:
		ip=i.split(" ")[0]
		iplist.append(ip)
		print(ip)

	print(iplist)	


	nodetype=Typenode()
	#taking name ip
	nnip=nodetype.radioip(iplist,'namenode')
	nnaddress=findadd(nnip,iplist,dockaddress)
	print(nnaddress)

	#taking datanode
	ddip=nodetype.checkip(iplist,'datanodes')
	ddaddress=findadd(ddip,iplist,dockaddress)
	print(ddaddress)

	#taking jobtracker
	jtip=nodetype.radioip(iplist,'jobtrackers')
	jtaddress=findadd(jtip,iplist,dockaddress)
	print(jtaddress)

	#taking tasktracker
	ttip=nodetype.checkip(iplist,'tasktrackers')
	ttaddress=findadd(ttip,iplist,dockaddress)
	print(ttaddress)

	#saving nodes names

	s.savenode(nnaddress,ddaddress,jtaddress,ttaddress)


	execfile("hadoopmenu.py")
	#showing nodenames
	#nnt,ddt,ttt,jtt=s.takenode()
