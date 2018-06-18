#!/usr/bin/python2

import cgi,commands

print "Content-type:text/html"
print ""

#taking data from apache(i.e. html) and storing it in web variable

web=cgi.FieldStorage()

#not interested in web page just the data from x

drive_name=web.getvalue("dn")
drive_size=web.getvalue("ds")

print drive_name
print drive_size

#checking for same name
check=commands.getoutput("ls /var/www/html/storage/")
#splitting on behalf of \n
check_1=check.split('\n') 

if drive_name in check_1:
	print "<h1>Drive Name already exists</h1></br>"
	print "<a href='http://192.168.122.67/object_storage.html'>"
	print "Click here to go back"
	print "</a>"	

else :
	#createing lv in host	
	#we have already created a vg named cloud and a pool named pool1
	commands.getoutput("sudo lvcreate --name "+drive_name+"  -V"+drive_size+"M --thin cloud/pool1")
	print "<pre>"
	print commands.getoutput("sudo lvdisplay")
	print "</pre>"
	#formatting on the vm 
	commands.getoutput("sudo mkfs.xfs /dev/cloud/"+drive_name)

	#making directory in /var/www/html so that it can be accessed from httpd protocol
	commands.getoutput("sudo mkdir /var/www/html/storage/"+drive_name)
	#print commands.getoutput("ls /var/www/html/")

	#mounting 
	commands.getoutput("sudo mount /dev/cloud/"+drive_name+" /var/www/html/storage/"+drive_name)


