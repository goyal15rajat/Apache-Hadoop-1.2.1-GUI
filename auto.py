import os
os.sTystem("cd /etc/hadoop ")

file1 =  open ("/home/rajat/Documents/copy.txt","r+",buffering=1)

file3 =  open ("/home/rajat/Documents/copy.txt","w+")
file2 =  open ("/home/rajat/Documents/orig.txt","a+")
strr = file1.read().split("\n")
print(strr)
print(type(strr))
for line in strr:
	if  line == "<value>2</value>":
		s = line.replace("<value>2</value>","AAAAAAAA")
		file3.write(s+"\n")
		print (s)
	else:
		file3.write(line+"\n")	
		print(line)


#	if line == ("<property>") :
#		print("hiuhsdks")
	#s.replace("<property>","aaaaaaaaaaaa")
	#print(s)
	
		
	#if str == "<value>2</value>":
	#	line.remove(str)
	#	line.append("AAAAAAAAA")
	#	file1.writelines(line)
	




#fo2 =open("/home/rajat/Documents/ww.txt","w+")

#str = fo.readline()

#for x in str:
#	print(x)
#	if x == "<value>2</value>":
#		print("$$$$$$$$$$$$$$$")

#		str.remove(x)


	
#fo2.writelines(str)		

	
#print str	
	

