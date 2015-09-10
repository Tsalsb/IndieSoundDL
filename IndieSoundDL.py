import urllib
import lxml.html
import subprocess
List = []
path = "-o ~/Desktop/%(title)s.%(ext)s"

abort = "--abort-on-error"

connection = urllib.urlopen('URL of site')

dom =  lxml.html.fromstring(connection.read())

for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
  if 'Keywork 1' or 'Keyword 2' in link: # Add keywords such as soundcloud or mixcloud
		List.append(link)
		for song in List:
		  cmds = ["youtube-dl",str(path),str(song)] #Pipe command into youtube-DL for download
		  subprocess.Popen(cmds)
		
print "Currently Downloading...",List
   
#youtube-dl OPTIONS (#options) URL [URL...]

#youtube-dl -o ~/Desktop/%(title)s.%(ext)s 'youtube file url'
