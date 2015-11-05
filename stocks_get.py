import urllib
import json
import time
import os

print "Please specify a time frame for data: "
print "Formats: 1D, 1M, 1Y" 
timeFrame=raw_input()

print "Please specify a file name: "
fileName = raw_input()

symbols = ["AAPL","TSLA","GOOG","NFLX","AMD","GE","F","GM","CDW","AMZN","NVDA","ATVI","DG","MOS","CF"]

newfile = open(fileName+'.csv','w')


i=0
while i<len(symbols):
	url = "http://www.bloomberg.com/markets/chart/data/"+timeFrame+"/"+symbols[i]+":US"
	htmltext = urllib.urlopen(url)
	data =json.load(htmltext)
	datapoints = data["data_values"]

	for point in datapoints:
		date = point[0]
		price = point[1]
		date = time.strftime('%m/%d/%Y %H:%M:%S',time.gmtime(int(date)/1000.))
		csv = symbols[i]+','+str(date)+','+str(price)+'\n'
		newfile.write(csv)
	i+=1
newfile.close()

print fileName+".csv has been created @ "+os.getcwd() 