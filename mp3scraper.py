
import urllib2
import re
from bs4 import BeautifulSoup

url = "http://www.example.com/"
page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page)

#links = soup.find_all('a') #, href=re.compile('$mp3'))
#links = soup.find_all('a', href=re.compile('(?i)(mp3)$'))
#links = soup.find_all('a', href=re.compile('(mp3|mp3 )$'))
links = soup.find_all('a', href=re.compile(r'mp3'))

for link in links:
	linkName = link.contents[0]
	fullLink = link.get('href')
	print fullLink
	print linkName
