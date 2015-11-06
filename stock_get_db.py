import urllib
import json
import time
import os
import includes
import config
import mysql.connector

#dbinfo
conn=mysql.connector.connect(user='root',password='root',host='localhost',database='stocks')
dbc=conn.cursor()


#just getting info from user
print '\n\n'
print "This program scrapes and loads a list of stocks from the web to a database."+'\n\n'
print "Please specify a time frame for data: "
print "Formats: 1D, 1M, 1Y"+'\n' 
timeFrame=raw_input('-->')

print "Please select extract type- CSV or DB: "+'\n'
extractType=raw_input('-->')

start_time = time.clock()

#add stocks here to pull into csv
symbols = ["AAPL","TSLA","GOOG","NFLX","AMD","GE","F","GM","CDW","AMZN","NVDA","ATVI","DG","MOS","CF",
			"IFON","GE","BAC","FL","UBNT","RAI","MO","CRAY","FB","AKAM","CAT","INTC","IBM","DIS","COKE","CMG"]


if extractType=='DB':	
	print "Please wait..."+'\n'
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
			date = includes.convepoch(date)
			count +=1
			dbc.execute("INSERT INTO stocks.ticks (symbol,time,price) VALUES ('"+symbols[i]+"','"+date+"','"+str(price)+"');")
		i+=1
	conn.commit()

	print "Operation completed sucessfully:"+'\n'
	print "Number of stocks scraped "+str(i)+'\n'
	print "Number of lines imported "+str(count)+'\n'
	print "Time taken... "+str(round(time.clock() - start_time,3)), "seconds"+'\n'
else:
	print "Please specify a file name:"
	print "all files automaticly export as a .csv file."+'\n'
	fileName = raw_input('-->')
	newfile = open(fileName+'.csv','w')
	print '\n'
	print "Please wait..."+'\n'
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
			date = includes.convepoch(date)
			csv = symbols[i]+','+str(date)+','+str(price)+'\n'
			newfile.write(csv)
			count +=1
		i+=1
	newfile.close()

	print "Operation completed sucessfully:"+'\n'
	print "Number of stocks scraped "+str(i)+'\n'
	print "Number of lines written "+str(count)+'\n'
	print "Time taken... "+str(round(time.clock() - start_time,3)), "seconds"+'\n'
	print fileName+".csv has been created @ "+os.getcwd()+'\n'

