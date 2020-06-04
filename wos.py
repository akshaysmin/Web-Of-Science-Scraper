import requests
from bs4 import BeautifulSoup
#from pprint import pprint
import webbrowser

'''
this program extracts information from all pages in a web of science search, given first page url, and saves it in file line by line
companion program words.py collects important info from saved file
'''

start_url=input("Enter url of first results page")
#end_url=''
#temp=''

#print(soup)
def scrap_page(url):
	page=requests.get(url)
	print(page)
	soup=BeautifulSoup(page.text,'lxml')

	results=soup.find_all('div',class_='search-results-item')
	c=''
	for item in results:
		no=item.find_all('div',class_='search-results-number')[0].text.strip()
		content=item.find_all('div',class_='search-results-content')[0].find_all('div')
		title=content[0].text.strip()
		authors=content[2].text.strip()
		p_info=content[3].text.strip().replace('\n',' ')
		citations=item.find_all('div',class_='search-results-data-cite')[0].text.replace('Times Cited: ','').replace(' (from Web of Science Core Collection)','').strip()
		c+='\n'+no+'\n'+title+'\n'+authors+'\n'+p_info+'\n'+citations
		#print(citations)
		c+='\n###'
	with open('results.txt','a') as f:
		f.write(c)
	print(c)
	next_url=soup.find_all('a',title='Next Page')[0]['href']
	print('returning url for next page')
	url=next_url
	return url
#mainblock
url=start_url
not_end=True
i=1
while not_end:
	print('now on',i,'th page')
	url=scrap_page(url)
	i+=1




