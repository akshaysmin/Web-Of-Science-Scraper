filename='results.txt'
'''

companion program wos.py extracts information from all pages in a web of science search, given first page url, and saves it in file line by line
this program collects important info from saved file

present Problem : last search result not extracted

#format of each chunk:
no.
title
authors
publication info + date
citations
'''
num_lines=6
title_n=1
author_n=2
pub_n=3
cit_n=4

class s_result:
	s_items=[]#search_items
	d_not_found_texts=[]
	def __init__(self,title,authors,citations,date,pub):
		self.title=title
		self.authors=authors
		self.citations=citations
		self.date=date
		self.pub=pub

def formatdate(d):
	d=d[-1:]+d[:-1]
	return d

def finddate(text):
	start_string='Published:'
	end_strings=[str(i) for i in range(2000,2030)]
	if start_string not in text:
		print('Start string not found')
		s_result.d_not_found_texts.append(text)
		return 'None'
	i_=text.index(start_string)+len(start_string)
	j=i_
	for i in range(i_,i_+10):
		if text[i:i+4] in end_strings:
			j=i+4
	if j==i_:
		print('End string not found')
		s_result.d_not_found_texts.append(text)
		return 'None'
	datetext=' '.join(formatdate(text[i_:j].split()))
	print(datetext)
	return datetext

def sanitycheck(datalist):
	boo=True
	line_no=[]
	for i,text in enumerate(datalist):
		if text=='###\n':
			if i%num_lines!=num_lines-1:
				boo=False
				line_no.append(i)			
	return boo,line_no

def extractinfo(data):
	for i,text in enumerate(data):
		#print(i,line)
		if i%num_lines==title_n:
			title=text.replace('\n',' ').strip()
		if i%num_lines==author_n:
			author=text.replace('\n',' ').strip()
		if i%num_lines==pub_n:
			date=finddate(text)
			pub=text.replace('\n',' ').strip()
		if i%num_lines==cit_n:
			cit=text.replace('\n',' ').strip()
		if i%num_lines==0 and i!=0:
			s_result.s_items.append(s_result(title,author,cit,date,pub))

def print_obj_data():
	print('citations')
	for item in s_result.s_items:
		print(item)
		print('\n' in item.title)
		print('\n' in item.authors)
		print('\n' in item.citations)
		print('\n' in item.date)

def makexl(search_obj_list,filename,delimeter='	'):
	with open(filename,'w') as f:
		for obj in search_obj_list:
			text=delimeter.join([obj.date,obj.citations,obj.title,obj.authors,obj.pub])+'\n'
			f.write(text)
	return None
#main code

with open(filename,'r') as f:
	data=f.readlines()

while '\n' in data:
	data.remove('\n')

print(sanitycheck(data))
print(len(data)/1547)

extractinfo(data)

#print(print_obj_data())
print(len(s_result.s_items))

print(makexl(s_result.s_items,'resultsxl.txt'))

print('all done !')









