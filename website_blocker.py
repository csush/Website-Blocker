import time
from datetime import datetime as dt

#Path to host file
#Copied etc/hosts to project dir for testing purposes
host_path = "etc/hosts"

#Redirect to local host
redirect = "127.0.0.1"

#List of websites to block
website_list = ["www.netflix.com", "www.facebook.com"]

while True:
	#dt method takes current date and you input 8 & 16 and compare with current time
	if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
		print("Work")

		#Opening hosts file
		file = open(host_path, 'r+')

		#Reading hosts file into content variable
		content = file.read()

		#Check and write if websites which need to be blocked are in content
		for website in website_list:
			if website in content:
				pass
			else:
				file.write(redirect + " " + website + "\n")

	else:
		print("Play")

		file = open(host_path, 'r+')

		#content reads all lines of file
		content = file.readlines()

		file.seek(0)

		for line in content:
			if not any(website in line for website in website_list):
				file.write(line)
			file.truncate()
	time.sleep(2)
