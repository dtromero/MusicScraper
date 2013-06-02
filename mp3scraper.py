import os
import re
import urllib2
from bs4 import BeautifulSoup

def urlmp3downloader(url,dlmusicfolder):
	# The following code uses urllib2 and BeautifulSoup to open, read and extract all the <a> tag links with '.mp3' to the links variable
	page = urllib2.urlopen(url).read()
	soup = BeautifulSoup(page)
	links = soup.find_all('a', href=re.compile(r'.mp3'))

	# Checks to see if the dlmusicfolder path already exists. If not, it will create that directory to put the files
	if not os.path.exists(dlmusicfolder):
		os.makedirs(dlmusicfolder)

	# Initialize loop for each of the '.mp3' links
	for link in links:
		# Initialized four local variables: songName, fileName, fullLink and musicfilePath
		# -- songName stores set to the text between the <a></a> tags. 
		# -- file name stores the songName text, performs basic character escaping and appends the .mp3 file extension
		# -- fullLink stores the link location for the file being downloaded
		# -- musicfilePate creates and stores the full filepath and name for the mp3 being downloaded
		songName = link.contents[0]
		fileName = songName.replace("/","").replace("\\","") + ".mp3"
		fullLink = link.get('href')
		musicfilePath = os.path.join(dlmusicfolder,fileName)
	
		# Checks if the file has been previously downloaed
		if not os.path.exists(musicfilePath):
			# Prints the string for file being downloaded and the filepath
			print "Downloading: " + fullLink + " | To: " + musicfilePath
			# Opens the link using urllib2
			f = urllib2.urlopen(fullLink)
			# writes the opened file to disk
			with open(os.path.join(musicfilePath), "wq") as local_file:
				local_file.write(f.read())
	
		# If the file already exists (has been previously downloaded) prints following string imforming the user
		else: print fileName  + " has already been downloaded!"

# Accepts and iterates through a list of (x,y) values where:
# x is the website and
# y is the filepath
def multisitemp3(sitelist):
	for (x,y) in sitelist:
		n = len(x)
		print  (n+24)*"-" + "\n" + "| Checking " + x + " for mp3s.. |" + "\n" + (n+24)*"-" 
		urlmp3downloader(x,y)
	
