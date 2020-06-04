from pprint import pprint
import sys
'''
uses : 'resultsxl.txt'
goal : create a dictionary with keys as year and values as no. of titles with given term published in respective years
design: a counter for "term in title" while looping through each data row for each "year"
'''

filename='resultsxl.txt'
term='solution'
if len(sys.argv)>1:
	terms=[word.lower() for word in sys.argv[1:]]


with open(filename,'r') as f:
	data=f.readlines()
	#print(data)

dates={}

for line in data:
	#print(line)
	info=line.split('	')
	date=info[0][0:4]
	title=info[2].lower()
	n=0
	for term in terms:
		if term in title:
			n=1
			break	#n=0 means title doesn't contain any of the terms and n=1 means title contains atleast one of them
	if date!='None':
		date=int(date)
	if date not in dates:
		dates[date]=n
	else:
		dates[date]+=n
print('search terms: ',terms)
pprint(dates)
	
	

