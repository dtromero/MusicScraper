import os
import re
import urllib2
from bs4 import BeautifulSoup

# Initializing two variables: url and musicfolder. 
# -- url contains the address to the website that you would like to download mp3's from
# -- musicfolder is the local file folder that each mp3 will be downloaded to
url = "http://www.example.com/"
musicfolder = "/home/user/Music/example"

# The following code uses urllib2 and BeautifulSoup to open, read and extract all the <a> tag links with '.mp3' to the links variable
page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page)
links = soup.find_all('a', href=re.compile(r'.mp3'))

# Checks to see if the musicfolder path already exists. If not, it will create that directory to put the files
if not os.path.exists(musicfolder):
	os.makedirs(musicfolder)

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
	musicfilePath = os.path.join(musicfolder,fileName)
	
	# Checks if the file has been previously downloaed
	if not os.path.exists(musicfilePath):
		# Prints the string for file being downloaded and the filepath
		print "Downloading: " + fullLink + " | To: " + musicfilePath
		# Opens the link using urllib2
		f = urllib2.urlopen(fullLink)
		# writes the opened file to disk
		with open(os.path.join(musicfolder,fileName), "wq") as local_file:
			local_file.write(f.read())
	
	# If the file already exists (has been previously downloaded) prints following string imforming the user
	else: print fileName  + " has already been downloaded!"
