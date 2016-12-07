#!/usr/bin/python
import commands,os


class Typenode():
	def radioip(self,iplist,who):
		x = ' FALSE '.join(iplist)
		choice = (list(commands.getstatusoutput("zenity --list --title='choose "+who+"' --radiolist --column 'Pick' --column 'IP' FALSE" +" "+x)))[1].split("\n")[1].split('|')
		return(choice)

	def checkip(self,iplist,who):
		x = ' FALSE '.join(iplist)
		choice = (list(commands.getstatusoutput("zenity --list --title='choose "+who+"' --checklist --column 'Pick' --column 'IP' FALSE" +" "+x)))[1].split("\n")[1].split('|')
		return(choice)

class Node():

	def formatnn(self,nlist):
		for i in nlist :
			os.system("docker exec -it "+i+" hadoop namenode -format")
	
	def startdaemon(self,nlist,daemon):
		for i in nlist :

			#os.system("docker exec -it "+i+" 'cp /home/Untitled\ Folder/hdfs-site.xml   /etc/hadoop'")
			#os.system("docker exec -it "+i+" 'cp /home/Untitled\ Folder/core-site.xml   /etc/hadoop'")
			print("starting")
			os.system("docker exec -it "+i+" hadoop-daemon.sh start "+daemon+" ")
			print("started")
		

#class Namenode():
'''def startnn(self,nn):
		os.system("docker exec -it "+nn+" 'cp /root/prog/hdfs-site.xml   /etc/hadoop'")
		print("starting nn")
		os.system("docker exec -it "+nn+" 'hadoop-daemon.sh start namenode'")
		print("started nn")
'''	

#class Datanode():
'''	def startdd(self,dd):
		print("docker exec -it "+dd+ " 'starting dd")
		os.system("hadoop-daemon.sh start datanode")
		print("started dd") 
'''		
