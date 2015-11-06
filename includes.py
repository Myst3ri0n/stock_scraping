import time

#converts epch date
def convepoch(date):
	return time.strftime('%m-%d-%Y %H:%M:%S',time.gmtime(int(date)/1000.))