import os
import urllib2
import re
from bs4 import BeautifulSoup

url = "http://www.example.com/"
urltag = "example"
filepath = "/home/user/Music/"

musicfolder = os.path.join(filepath,urltag)
page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page)

links = soup.find_all('a', href=re.compile(r'mp3'))

if not os.path.exists(musicfolder):
	os.makedirs(musicfolder)

for link in links:
	linkString = link.contents[0]
	linkName = linkString.replace("/","").replace("\\","") + ".mp3"
	fullLink = link.get('href')
	print "Downloading: " + linkName + " | To: " + filepath + urltag
	
	f = urllib2.urlopen(fullLink)

	with open(os.path.join(musicfolder,linkName), "wq") as local_file:
		local_file.write(f.read())
