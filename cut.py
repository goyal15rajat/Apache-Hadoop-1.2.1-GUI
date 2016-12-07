import os,commands

c1 = commands.getstatusoutput("systemctl restart docker")
#print(c1)
c2 = commands.getstatusoutput("docker images |cut -d' ' -f1")
print(c2)
print(type(c2))
print(c2[1])
print(type(c2[1]))
l = c2[1].split('\n')
l.remove("REPOSITORY")
print("printing l")
print(l)
print(type(l))
#for x in l:
#	if x != 'REPOSITORY':
#		print(x)
#	else:
#		continue