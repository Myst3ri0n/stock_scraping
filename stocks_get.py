import urllib
import json
import time

symbols = ["AAPL","TSLA","GOOG","NFLX","AMD","GE","F","GM"]

newfile = open('stocks.csv','w')

print "Please specify a time frame for data: "
print "Formats: 1D, 1M, 1Y" 

timeFrame=raw_input()

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