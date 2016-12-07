#!/usr/bin/python
import commands,os
from Edit import *

class Doc():

	def makedoc(self,system) :
		docklist = []
		for i in range(0,system) :
			os.system("docker run --privileged=true -dit hcent7 /bin/bash")
			dockname=commands.getstatusoutput("docker ps -a|head -2|grep cent7|awk {'print $NF'}")[1]
			print(dockname)
			docklist.append(dockname)

		print(docklist)
		return (docklist)

	def ipdoc(self,doclist):
		dockip=[]
		dockaddress=[]
		for i in doclist:
			docip = commands.getstatusoutput("docker exec -it "+i+" 'ifconfig'|grep inet|head -1|awk '{print$2}'")[1]
			dockip.append(docip)
			dockaddress.append(docip+" "+i)

		print(dockaddress)	

		return(dockaddress)	


	def copy_core(self,doclist,nnip):

		for i in doclist :
			os.system('docker cp '+i+':/etc/hadoop/core-site.xml /tmp/ ')
			print("copied to /tmp/")
			e=Edit_core()
			e.core_nn(nnip)
			os.system('docker cp /tmp/core-site.xml  '+i+':/etc/hadoop/ ')
			print("copied to "+i)


	def cop_core(self,doclist):

		for i in doclist :
			os.system('docker cp /tmp/core-site.xml  '+i+':/etc/hadoop/ ')
			print("copied to "+i)

	def client_core(self):
		os.system('cp /tmp/core-site.xml  /etc/hadoop/ ')


	def jt_core(self,doclist,nnip):

		for i in doclist :
			os.system('docker cp '+i+':/etc/hadoop/core-site.xml /tmp/ ')
			print("copied to /tmp/")
			e=Edit_core()
			e.core_nn(nnip)
			os.system('docker cp /tmp/core-site.xml  '+i+':/etc/hadoop/ ')
			print("copied to "+i)


	def tt_mapred(slef,doclist,jtip):

		for i in doclist :
			os.system('docker cp '+i+':/etc/hadoop/mapred-site.xml  /tmp/ ')
			print("copied to /tmp/")
			e=Edit_mapred()
			e.mapred_t(jtip)
			os.system('docker cp /tmp/mapred-site.xml  '+i+':/etc/hadoop/ ')
			print("copied to "+i)

	def cop_mapred(self,doclist):

		for i in doclist :
			os.system('docker cp /tmp/mapred-site.xml  '+i+':/etc/hadoop/ ')
			print("copied to "+i)		

	def client_mapred(self):
		os.system('cp /tmp/mapred-site.xml  /etc/hadoop/ ')			

'''	def tt_core(self,doclist):

		for i in doclist :
			os.system('docker cp /tmp/core-site.xml  '+i+':/etc/hadoop/ ')
			print("copied to "+i)
'''						