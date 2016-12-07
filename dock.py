import commands
x = commands.getstatusoutput('systemctl restart docker')

#image name
f1 = commands.getstatusoutput("docker images|awk '{ print$1 }'")
l1 = f1[1].split("\n")
l1.remove('REPOSITORY')
print(l1)

#images
f2 = commands.getstatusoutput("docker images|awk '{ print$3 }'")
l2 = f2[1].split("\n")
l2.remove('IMAGE')
print(l2)