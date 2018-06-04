#!/usr/bin/python2
import time,os

x='''
THIS IS MY FIRST CLOUD CODE.
'''
print x
y='''
Press 1: To Run VLC
Press 2: To Run FIREFOX
Press 3: To Run CALCULATOR''' 
print y

choice=raw_input("enter your choice  :  ")
again='y'

while again=='y':
	

	if choice=='1':
		print "starting vlc..."
		time.sleep(2)
		user=raw_input("enter cloud user:  ")
		os.system("ssh -l "+user+" 192.168.122.1 -X vlc")
	elif choice=='2':
		print "starting firefox..."
		time.sleep(2)
		user=raw_input("enter cloud user:  ")
		os.system("ssh -l "+user+" 192.168.122.1 -X firefox")

	elif choice=='3':
		print "starting calculator..."
		time.sleep(2)
		user=raw_input("enter cloud user:  ")
		os.system("ssh -l "+user+" 192.168.122.1 -X gnome-calculator")

	else :
		print "Wrong choice!!!"
	again=raw_input("do you want to enter again(y/n):  ") 
	
	if again=='y':
		print y
		choice=raw_input("enter your choice  :  ")
	elif again=='n'
		print  "closing  programe   "
		time.sleep(2)
		exit()

