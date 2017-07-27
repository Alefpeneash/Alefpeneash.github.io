import html 
import cgi
from urllib.request import urlopen

form = cgi.FieldStorage()
lat = form.getfirst("LAT", "")
_long = form.getfirst("LONG", "")
radius = form.getfirst("RAD", "")

url = 'https://api.vk.com/method/photos.search.xml?lat='+str(lat)+'&long='+str(_long)+'&radius='+str(radius)

xml = urlopen(url).read()
f = open('C:\learning\VkGeotag\src\photos.search.xml', 'wb')
f.write(xml)
f.close()

print("Content-type: text/html")
print()
print('<meta http-equiv="refresh" content="0;URL=http://localhost:8000/cgi-bin/out.py" />')