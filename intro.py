#!/usr/bin/python

'''

_____________________                              _____________________
`-._:  .:'   `:::  .:\           |\__/|           /::  .:'   `:::  .:.-'
    \      :          \          |:   |          /         :       /    
     \     ::    .     `-_______/ ::   \_______-'   .      ::   . /      
      |  :   :: ::'  :   :: ::'  :   :: ::'      :: ::'  :   :: :|      
      |     ;::         ;::         ;::         ;::         ;::  | :DEVELOPED BY - RAJAT      
      |  .:'   `:::  .:'   `:::  .:'   `:::  .:'   `:::  .:'   `:|      
      /     :           :           :           :           :    \      
     /______::_____     ::    .     ::    .     ::   _____._::____\      
                   `----._:: ::'  :   :: ::'  _.----'                    
                          `--.       ;::  .--'                          
                              `-. .:'  .-'                              
                                 \    /                          
                                  \  /                                  
                                   \/  
'''


import os,commands
from sqlcon import *
from login import *

choice = commands.getstatusoutput("zenity --list --title='Chose ur option' --column='Choice'  LOGIN 'SIGN UP' EXIT")
print(choice[1])
rchoice = choice[1].split("\n")
if rchoice[1] == 'LOGIN':
	print("choice 1")
	u=Userdetails()
	u.setuname()
elif  rchoice[1] == 'SIGN UP':
	print("choice 2")
	execfile("signup.py")
else:
	os.system("exit") 

