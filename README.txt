project goal:
1.search a term in web of science and
2.extract metadata from all the search results and
3.store metadata in the file 'results.txt' and
4.structure 'results.txt' to create 'resultsxl.txt' for further analysis

script files:
1.'wos.py' -- for steps 1-3
2.'words.py' -- for steps 4
3.'dateVsTermInTitle.py' -- print dictionary with {<date>:<no. of titles with term>}

output files created:
1.'results.txt' -- from 'wos.py'
2.'resultsxl.txt' --from 'words.py'

script related notes:
1.'wos.py' related:
	1.copy paste fresh url from net as start url
	2.for each result page metadata is extracted as lines, then adds it to 'results.txt' in append mode
	3.in one search result page, for each search result, 5 lines are extracted as
		0.<newline>
		1.Sl.No.
		2.title
		3.authors
		4.other info - journal,publisher,citation info,date,...
		5.no. of citations
2.'words.py' related:
	Problem : doesn't include last search result from 'results.txt'

