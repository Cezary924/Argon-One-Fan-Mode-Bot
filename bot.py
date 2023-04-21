import os, time
from datetime import datetime
dir = os.path.dirname(os.path.realpath(__file__)) + "/"
sleep_time = 60

#------------------------------

def first_mode(now, day, boot):
	try:
		with open(dir + "files/first_mode.txt", "r") as f:
			out_str = f.read()
	except OSError:
		print("Open error: first_mode.txt file")
		exit(1)
	#out_str = "45=20\n50=40\n55=60\n60=80\n65=100\n"
	
	try:
		f = open("/etc/argononed.conf", "w")
		f.write(out_str)
		f.close()
	except OSError:
		print("Open error: argononed.conf file")
		exit(1)
	
	os.system("sudo systemctl restart argononed.service")
	
	day = True
	boot = True
	print(now.strftime("%H") + ":" + now.strftime("%M") + " - Fan's first mode has been activated.")
	return day, boot

def second_mode(now, day, boot):
	try:
		with open(dir + "files/second_mode.txt", "r") as f:
			out_str = f.read()
	except OSError:
		print("Open error: second_mode.txt file")
		exit(1)
	#out_str = "55=33\n60=67\n65=100\n"
	
	try:
		f = open("/etc/argononed.conf", "w")
		f.write(out_str)
		f.close()
	except OSError:
		print("Open error: argononed.conf file")
		exit(1)
	
	os.system("sudo systemctl restart argononed.service")
	
	day = False
	boot = True
	print(now.strftime("%H") + ":" + now.strftime("%M") + " - Fan's second mode has been activated.")
	return day, boot

#------------------------------

boot = False
day = False
start = ""
stop = ""

try:
	with open(dir + "files/start.txt", "r") as f:
		start = f.read()
except OSError:
	print("Open error: start.txt file")
	exit(1)

try:
	with open(dir + "files/stop.txt", "r") as f:
		stop = f.read()
except OSError:
	print("Open error: stop.txt file")
	exit(1)

start = int(start)
stop = int(stop)

while True:
	now = datetime.now()
	hour = now.hour
	
	if boot == True:
		if start <= hour and hour < stop:
			if day == False:
				day, boot = first_mode(now, day, boot)
			else:
				print(now.strftime("%H") + ":" + now.strftime("%M") + " - No changes in fan's behaviour.")
		else:
			if day == False:
				print(now.strftime("%H") + ":" + now.strftime("%M") + " - No changes in fan's behaviour.")
			else:
				day, boot = second_mode(now, day, boot)
	else:
		if start <= hour and hour < stop:
			day, boot = first_mode(now, day, boot)
		else:
			day, boot = second_mode(now, day, boot)
	
	time.sleep(sleep_time)
