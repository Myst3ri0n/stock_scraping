import time

#converts epch date
def convepoch(date):
	return time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime(int(date)/1000.))

def nowDatetime():
	return (time.strftime("%Y-%m-%d %H:%M:%S"))

#Prints file linecount (Excluding White Space)
def lineCount(txtFile):
	num_lines = sum(1 for line in open(txtFile	))
	print num_lines
	return num_lines
