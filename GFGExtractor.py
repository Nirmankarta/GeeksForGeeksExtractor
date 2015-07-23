from bs4 import BeautifulSoup
import urllib2
import os.path
import string
from R2D2 import *
import codecs

#R2D2.py contains functions to customize output.

menu = ['c','fundamentals-of-algorithms','data-structures','c','c-plus-plus','java']

#path = ""      # Specify your path here
#path = "E:\GeeksForGeeks\\" 	#Sample windows path
path = "/home/nirmankarta/Pictures/GFG/new/" 	#Sample linux path

basicHTML = "<html><head><title>Index</title></head><body>"


def main():	
	print 'GeeksforGeeks Website Extractor'

	n = 0

	rootIndex = basicHTML + '<h3>GeeksforGeeks</h3>'
	for item in menu:	
		print	
		url = "http://www.geeksforgeeks.org/" + item +"/"
		log('\tRetrieving {0} of {1}: {2}'.format(n+1,len(menu),item))
		try:		
			data = urllib2.urlopen(url).read()
		except urllib2.HTTPError, err:
		   if err.code == 404:
		       log("{0} of {1}: 404: Page not found! | {2}".format(n+1,len(menu),url),2)
		   elif err.code == 403:
		       log("{0} of {1}: 403: Access denied! | {2}".format(n+1,len(menu),url),2)
		   else:
		       log("{0} of {1}: Something happened! Error code: {2} | {3}".format(n+1,len(menu),err.code,url),2)
		except urllib2.URLError, err:
		    log("\t{0} of {1}: Some other error happened: {2} | {3}".format(n+1,len(menu),err.reason,url),2)

		soup = BeautifulSoup(data)
		allLinks = soup.find("div",attrs={'class':'entry-content'}).findAll('li')
		listofLinks = []
		
		for link in allLinks:
			mainLink = link.find('a')['href']
			if(mainLink[0] not in ('#')):
				listofLinks.append(mainLink)
		Extract_And_Save_Page_Data('http://geeksquiz.com/',item, listofLinks,path)
		n = n + 1
		rootIndex += '<a href="' + item + '/index.html">' + item +'</a><br/>'
	rootIndex += '</body></html>'
	log(path,1)
	with open(path + "/index.html","wb") as f:
		f.write(str(rootIndex))	


def Extract_And_Save_Page_Data(url,dir_name,listofLinks,path):
	n = 0
	listofTitles = []
	pageTitle = 'NA'
	indexData = basicHTML + '<h3>' + dir_name + '</h3>'
	if not os.path.exists(path+dir_name):
		os.mkdir(path+dir_name)
	for item in listofLinks:
		pageName = item[:-1]
		pageName = pageName.split('/')
		pageName = pageName[len(pageName)-1]
		pageName = pageName+".html"
		filePath = path + dir_name[0:] +"/" +pageName
		n += 1
		if os.path.isfile(filePath):
			log('\t{0} of {1}: {2} exists!'.format(n, len(listofLinks), pageName))
		else:
			pageData = ""
			try:		
				pageData = urllib2.urlopen(item).read()
				page_soup = BeautifulSoup(pageData)
				pageTitle = page_soup.title.string
				pageTitle = pageTitle.replace(" - GeeksforGeeks","");
				with open(filePath,"wb") as f:
					f.write(str(pageData))		
				log('\t{0} of {1}: {2} is saved!'.format(n, len(listofLinks), pageName),1)
			except urllib2.HTTPError, err:
			   if err.code == 404:
			       log("\t{0} of {1}: 404: Page not found! | {2}".format(n, len(listofLinks),item),2)
			   elif err.code == 403:
			       log("\t{0} of {1}: 403: Access denied! | {2}".format(n, len(listofLinks),item),2)
			   else:
			       log("\t{0} of {1}: Something happened! Error code: {2} | {3}".format(n, len(listofLinks),err.code,item),2)
			except urllib2.URLError, err:
			    log("\t{0} of {1}: Some other error happened: {2} | {3}".format(n, len(listofLinks),err.reason,item),2)
			indexData += '<a href="' + pageName + '">' + pageTitle +'</a><br/>'
	indexData += '</body></html>'
			
	with codecs.open(path + dir_name[0:] + "/index.html","wb") as f:
		f.write(str(indexData))	

if __name__ == "__main__":
  main()