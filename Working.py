import urllib
import lxml.html
import subprocess
List = []
path = "-o ~/Desktop/%(title)s.%(ext)s"

abort = "--abort-on-error"

connection = urllib.urlopen('https://www.mixcloud.com/jonnyvalive/sundaefundae-w-jonny5-6-24-2013-part-1/')

dom =  lxml.html.fromstring(connection.read())

for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
  if 'soundcloud' or 'SOUNDCLOUD' in link:
		List.append(link)
		for song in List:
		  cmds = ["youtube-dl",str(path),str(song)]
		  subprocess.Popen(cmds)
		
print "This is the list of items",List
   
#youtube-dl OPTIONS (#options) URL [URL...]

#youtube-dl -o ~/Desktop/%(title)s.%(ext)s 'youtube file url'
