import urllib
import json
import time
import os

#just getting info from user
print '\n\n'
print "This program scrapes and outputs a list of stocks from the web."+'\n\n'
print "Please specify a time frame for data: "
print "Formats: 1D, 1M, 1Y"+'\n' 
timeFrame=raw_input('-->')

print "Please specify a file name:"
print "all files automaticly export as a .csv file."+'\n'
fileName = raw_input('-->')
print '\n'
print "Please wait..."+'\n'

start_time = time.clock()

#add stocks here to pull into csv
symbols = ["AAPL","TSLA","GOOG","NFLX","AMD","GE","F","GM","CDW","AMZN","NVDA","ATVI","DG","MOS","CF"]



newfile = open(fileName+'.csv','w')


i=0
count = 0
while i<len(symbols):
	url = "http://www.bloomberg.com/markets/chart/data/"+timeFrame+"/"+symbols[i]+":US"
	htmltext = urllib.urlopen(url)
	data =json.load(htmltext)
	datapoints = data["data_values"]

	for point in datapoints:
		date = point[0]
		price = point[1]
		#converting epoch time to human readable
		date = time.strftime('%m/%d/%Y %H:%M:%S',time.gmtime(int(date)/1000.))
		csv = symbols[i]+','+str(date)+','+str(price)+'\n'
		newfile.write(csv)
		count +=1
	i+=1
newfile.close()

print "Operation completed sucessfully:"

print "Number of stocks scraped "+str(i)+'\n'
print "Number of lines written "+str(count)+'\n'
print "Time taken... "+str(round(time.clock() - start_time,3)), "seconds"+'\n'
print fileName+".csv has been created @ "+os.getcwd()+'\n' 
