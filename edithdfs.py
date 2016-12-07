import os


e = Edit()
file1 =  open("/home/rajat/Documents/copy.txt","r+")
strr = file1.readlines()

if choice == "1":
	e.replications()
elif choice == "2" :
	e.block_size()
else:
	os.system("exit()")



file3 =  open ("/home/rajat/Documents/copy.txt","w+")
file3.writelines(strr)