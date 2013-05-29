import os
import urllib2
import re
from bs4 import BeautifulSoup

url = "http://www.example.com/"
urltag = "example"
homemusicfolder = "/home/user/Music/"

musicfolder = os.path.join(homemusicfolder,urltag)
page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page)

links = soup.find_all('a', href=re.compile(r'mp3'))

if not os.path.exists(musicfolder):
	os.makedirs(musicfolder)

for link in links:
	fileString = link.contents[0]
	fileName = fileString.replace("/","").replace("\\","") + ".mp3"
	fullLink = link.get('href')
	
	musicfilePath = os.path.join(musicfolder,fileName)
	
	if not os.path.exists(musicfilePath):
		print "Downloading: " + fileName + " | To: " + musicfilePath
	
		f = urllib2.urlopen(fullLink)

		with open(os.path.join(musicfolder,fileName), "wq") as local_file:
			local_file.write(f.read())

	else: print fileName  + " has already been downloaded!"
