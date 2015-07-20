from bs4 import BeautifulSoup
import urllib2
import os.path
import string

menu = ['fundamentals-of-algorithms','data-structures','c','c-plus-plus','java']

path = ""      # Specify your path here
#path = "E:\GeeksForGeeks\\" 	#Sample windows path
#path = "/home/nirmankarta/" 	#Sample linux path

basicHTML = "<html><head><title>Index</title></head><body>"

def main():	
	print '\n\nGeeksforGeeks Website extracter'
	n = 0
	for item in menu:		
		url = "http://www.geeksforgeeks.org/" + item +"/"
		print '\nRetrieving {0} of {1}: {2}'.format(n+1,len(menu),item)
		try:		
			data = urllib2.urlopen(url).read()
		except urllib2.HTTPError, err:
		   if err.code == 404:
		       print "404: Page not found! | {0}".format(url)
		   elif err.code == 403:
		       print "403: Access denied! | {0}".format(url)
		   else:
		       print "Something happened! Error code: {0} | {1}".format(err.code,url)
		except urllib2.URLError, err:
		    print "Some other error happened: {0} | {1}".format(err.reason,url)

		soup = BeautifulSoup(data)
		allLinks = soup.find("div",attrs={'class':'entry-content'}).findAll('li')
		listofLinks = []
		for link in allLinks:
			mainLink = link.find('a')['href']
			if(mainLink[0] not in ('#')):
				listofLinks.append(mainLink)
				#print mainLink
		Extract_And_Save_Page_Data('http://geeksquiz.com/',item, listofLinks,path)
		n = n + 1

def Extract_And_Save_Page_Data(url,dir_name,listofLinks,path):
	n = 0
	listofTitles = []

	if not os.path.exists(path+dir_name):
		os.mkdir(path+dir_name)
	for item in listofLinks:
		pageName = item[:-1]
		pageName = pageName.split('/')
		pageName = pageName[len(pageName)-1]
		'''if 'http://www.geeksforgeeks.org/' not in item:
			pageName = item.replace("http://geeksquiz.com/", "");
		else:
			pageName = item.replace("http://www.geeksforgeeks.org/", "");'''
		pageName = pageName+".html"
		filePath = path + dir_name[0:] +"/" +pageName
		n += 1
		if os.path.isfile(filePath):
			print '\t{0} of {1}: {2} exists!'.format(n, len(listofLinks), pageName)
		else:
			pageData = ""
			try:		
				pageData = urllib2.urlopen(item).read()
				page_soup = BeautifulSoup(pageData)
				with open(filePath,"wb") as f:
					f.write(str(pageData))		
				print '\t{0} of {1}: {2} is saved!'.format(n, len(listofLinks), pageName)
			except urllib2.HTTPError, err:
			   if err.code == 404:
			       print "404: Page not found! | {0}".format(item)
			   elif err.code == 403:
			       print "403: Access denied! | {0}".format(item)
			   else:
			       print "Something happened! Error code: {0} | {1}".format(err.code,item)
			except urllib2.URLError, err:
			    print "Some other error happened: {0} | {1}".format(err.reason,item)
if __name__ == "__main__":
  main()
