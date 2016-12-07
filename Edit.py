#!/usr/bin/python
class Edit_hdfs():

	def __init__(self):
		file1 =  open("/etc/hadoop/hdfs-site.xml","r+")
		strr = file1.readlines()
		file1.close()


	def replications(self):
		print("enter the value of replications u want")
		replica = str(input("replications>> "))
		indi = strr.index("<name>dfs.replication</name>\n")
		print(indi)
		strr[indi+1]="<value>"+replica+"</value>\n"
		'''DEVELOPED BY-RAJAT'''
		file2 =  open ("/etc/hadoop/hdfs-site.xml","w+")
		file2.writelines(strr)
		file2.close()



	def block_size(self,x):
		print("enter the value of block size u want")
		size = str(input("size>> "))
		sindi = strr.index("<name>dfs.block.size</name>\n")
		print(sindi)
		strr[sindi+1]="<value>"+size+"</value>\n"
		
		file2 =  open ("/etc/hadoop/hdfs-site.xml","w+")
		file2.writelines(strr)
		file2.close()



class Edit_core():

	def __init__(self):
		global strr
		file1 =  open("/tmp/core-site.xml","r+")
		strr = file1.readlines()
		file1.close()

	def core_nn(self,nnip):
		global strr
		ipindi = strr.index("<name>fs.default.name</name>\n")
		strr[ipindi+1]="<value>hdfs://"+nnip+":1001</value>\n"

		print(strr)
		file2 = open ("/tmp/core-site.xml","w+")
		file2.writelines(strr)
		file2.close()

	'''def core_jt(self,nnip):
		global strr
		ipindi = strr.index("<name>fs.default.name</name>\n")
		strr[ipindi+1]="<value>hdfs://"+nnip+":1001</value>\n"
		DEVELOPED BY-RAJAT
		print(strr)
		file2 = open ("/tmp/core-site.xml","w+")
		file2.writelines(strr)
		file2.close()	'''

	

class Edit_mapred():

	def __init__(self):
		global strr
		file1 =  open("/tmp/mapred-site.xml","r+")
		strr = file1.readlines()
		file1.close()
	
	def mapred_t(self,jtip):
		global strr
		ipindi = strr.index("<name>mapred.job.tracker</name>\n")
		strr[ipindi+1]="<value>hdfs://"+jtip+":9001</value>\n"

		print(strr)
		file2 = open ("/tmp/mapred-site.xml","w+")
		file2.writelines(strr)
		file2.close()		


		
