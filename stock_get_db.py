import urllib
import json
import time
import os
import includes
import config
import mysql.connector
import re

#dbinfo
conn=mysql.connector.connect(user='root',password='root',host='localhost',database='stocks')
dbc=conn.cursor()


#just getting info from user
print '\n'
print "This program scrapes and loads a list of stocks from the web to a database."+'\n\n'

print "what operation would you like to preform:"+'\n'
print "1. Dowload stock prices to CSV."
print "2. Import stock prices into the database."
print "3. Import basic financials into the database."+'\n'
opSelect=raw_input('-->')


if opSelect =='1':
	print "Please specify a time frame for data: "
	print "Formats: 1D, 1M, 1Y"+'\n' 
	timeFrame=raw_input('-->')
	extractType='CSV'
elif opSelect =='2':
	print "Please specify a time frame for data: "
	print "Formats: 1D, 1M, 1Y"+'\n' 
	timeFrame=raw_input('-->')
	extractType='DB'
else:
	extractType='basicFin'

#start clock to see how long the program took.
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
			date = includes.convepoch(date)
			count +=1
			dbc.execute("INSERT INTO stocks.ticks2 (symbol,time,price) VALUES ('"+symbols[i]+"','"+date+"','"+str(price)+"');")
		i+=1
	conn.commit()

	print "Operation completed sucessfully:"+'\n'
	print "Number of stocks scraped "+str(i)+'\n'
	print "Number of lines imported "+str(count)+'\n'
	print "Time taken... "+str(round(time.clock() - start_time,3)), "seconds"+'\n'
elif extractType=='CSV':
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
else:
	print "Under Construction: Try again Soon!"
	

