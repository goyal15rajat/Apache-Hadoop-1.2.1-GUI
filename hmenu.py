#!/usr/bin/python
import os,commands
from ipsave import *
from nodes import *
from docker import *
from Edit import *


class Had():
	global nnname,ddname,jtname,ttname

	def __init__(self):
		global nnname,ddname,jtname,ttname
	
		s=Saveip()
		#showing nodenames
		nnt,ddt,ttt,jtt=s.takenode()


		d=Doc()

		l=[]
		l.append(nnt)
		nnip=d.ipdoc(l)[0].split(" ")[0]
		print(nnip)

		nodelist=list()

		nnname = nnt.split(" ")
		ddname = ddt.split(" ")
		ttname = ttt.split(" ")
		jtname = jtt.split(" ")

'''DEVELOPED BY-RAJAT'''
		nlist=[]
		nlist.extend(ddname)
		nlist.extend(nnname)
		print(nlist)

		nodelist=list(set(nlist))
		nodelist.remove(nnname[0])
		print(nodelist)	

		d.copy_core(nnname,nnip)
		d.cop_core(nodelist)
		d.client_core()
		d.jt_core(jtname,nnip)
		d.cop_core(ttname)
		
		#starting namenode
		n=Node()

		n.formatnn(nnname)
		n.startdaemon(nnname,"namenode")
		#starting datanode
		n.startdaemon(ddname,"datanode")
		#n.startdaemon(ttt)
		#n.startdaemon(jtt)
		l=[]
		l.append(jtt)
		jtip=d.ipdoc(l)[0].split(" ")[0]
		print(jtip)
		d.tt_mapred(jtname,jtip)
		d.cop_mapred(ttname)
		d.client_mapred()

	def Choose_file(self):
		l=commands.getstatusoutput("hadoop fs -ls / | awk '{print $(NF) }'")[1].split("\n")
		l.remove('items')
		print(l)
		print(type(l))
		x = ' '.join(l)
		filename=commands.getstatusoutput("zenity --list --title='Choose file' --column='Files'"+" "+x)[1].split("\n")[1]
		return(filename)	


	def up(self,who):

		filename=commands.getstatusoutput("zenity --file-selection --title='choose "+who+"'")[1].split("\n")[1]
		print(filename)
		return(filename)

	def hdfsupload(self,filename):
		os.system("hadoop fs -put "+filename+"  /")
		#os.system("docker exec -it "+nnname[0]+" hadoop fs -put "+filename+" /")
		print("uploaded")

	def filedelete(self):
		filename=self.Choose_file()
		print(filename)
		os.system("hadoop fs -rmr "+filename+"  /")
		
	def mapred_name(self,f):
		print(f)
		f=f.split('/')
		print(f[-1])
		f="python "+f[-1]

		return(f)

	def view_output(self,out_file):
		os.system('hadoop fs -cat /'+out_file+'/part-00000 > /tmp/'+out_file)
		os.system("zenity --text-info --title='OUTPUT' --filename=/tmp/"+out_file+"")
		
	def view(self):
		l=commands.getstatusoutput("hadoop fs -ls / | awk '{print $(NF) }'")[1].split("\n")
		l.remove('items')
		print(l)
		print(type(l))
		x = ' '.join(l)
		filename=commands.getstatusoutput("zenity --list --title='Choose file' --column='Files'"+" "+x)[1].split("\n")[1]
		i=l.index(filename)
		print(i)
		m = commands.getstatusoutput("hadoop fs -ls / | awk '{print $(N1) }'")[1].split("\n")
		m.remove('Found')

		if m[i][0] == 'd':
			self.inview(filename)
		else:
			os.system('hadoop fs -cat /'+filename+' > /tmp/'+filename)
			os.system("zenity --text-info --title='OUTPUT' --filename=/tmp/"+out_file+"")

	def inview(self,filename):
		m = commands.getstatusoutput("hadoop fs -ls /"+filename+" | awk '{print $(NF) }'")[1].split("\n")

		


		

	def mrrun(self):
		global nnname,ddname,jtname,ttname
		n=Node()
		n.startdaemon(ttname,"tasktracker")
		
		n.startdaemon(jtname,"jobtracker")

		print("mapred is running")
		print(jtname)
		print(ttname)
		#chosing file to apply mapred
		hadoop_file=self.Choose_file()

		mapper=self.up("mapper")
		reducer=self.up("reducer")
	
		mapper_file=self.mapred_name(mapper)
		reducer_file=self.mapred_name(reducer)
		print(mapper_file)
		print(reducer_file)

		out_name=commands.getstatusoutput("zenity --entry --title='OUTPUT FILE' --text='Enter name of output file'")[1].split("\n")[1]

		os.system("hadoop jar /usr/share/hadoop/contrib/streaming/hadoop-streaming-1.2.1.jar  -input "+hadoop_file+" -file "+mapper+"   "+reducer+"   -mapper  '"+mapper_file+"' -reducer '"+reducer_file+"'  -output /"+out_name+"")
		self.view_output(out_name)