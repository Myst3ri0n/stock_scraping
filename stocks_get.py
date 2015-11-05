import urllib
import json
import time

symbols = ["AAPL","TSLA","GOOG","NFLX","AMD","GE","F","GM"]

i=0
while i<len(symbols):
	url = "http://www.bloomberg.com/markets/chart/data/1D/"+symbols[i]+":US"
	htmltext = urllib.urlopen(url)
	data =json.load(htmltext)
	datapoints = data["data_values"]

	for point in datapoints:
		date = point[0]
		price = point[1]
		date = time.strftime('%m/%d/%Y %H:%M:%S',time.gmtime(int(date)/1000.))
		print date," - ",price

	print symbols[i]," number of data points", len(datapoints)
	i+=1