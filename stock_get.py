import urllib
import json
import time


htmltext = urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1D/AAPL:US")

data =json.load(htmltext)

datapoints = data["data_values"]

for point in datapoints:
	date = point[0]
	price = point[1]
	date = time.strftime('%m/%d/%Y %H:%M:%S',time.gmtime(int(date)/1000.))
	print date," - ",price

print "# of data points", len(datapoints)