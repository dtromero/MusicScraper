
import urllib2
import re
from bs4 import BeautifulSoup

url = "http://www.aquariumdrunkard.com"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

links = soup.find_all('a') #, href=re.compile('$mp3'))

for link in links:
	#linkName = link.contents[0]
	fullLink = link.get('href')
	print fullLink
