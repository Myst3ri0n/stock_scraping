import time

#converts epch date
def convepoch(date):
	return time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime(int(date)/1000.))

def nowDatetime():
	return (time.strftime("%Y-%m-%d %H:%M:%S"))
