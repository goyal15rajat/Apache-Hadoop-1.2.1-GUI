print("enter the value of replications u want")
replica = str(input(">>"))
file1 =  open ("/home/rajat/Documents/copy.txt","r+")

strr = file1.read().split("\n")
print(strr)
z =[]
print(type(strr))
for line in strr:
	if  line == "<value>34</value>":
		s = line.replace("<value>34</value>","<value>"+replica+"</value>")
		z.append(s)
		z.append("\n")
	else:
		z.append(line)
		z.append("\n")
		
print(z)
file3 =  open ("/home/rajat/Documents/copy.txt","w+")
for y in z:
	print (y)
	file3.write(y)
file1.close()