from urllib.request import urlopen
from PIL import Image
import xml.etree.ElementTree as etree
import time 

tree = etree.parse('C:/learning/VkGeotag/src/photos.search.xml')
root = tree.getroot()

owner_id = tree.findall('owner_id')
pid = tree.findall('pid')
src_big = tree.findall('src_big')
src_xbig = tree.findall('src_xbig')
src_xxbig = tree.findall('src_xxbig')
src_xxxbig = tree.findall('src_xxxbig')
lat = tree.findall('lat')
_long = tree.findall('long')
width = tree.findall('width')
height = tree.findall('height')
created = tree.findall('created')
size_big = 604 * 604
size_xbig = 807 * 807 
size_xxbig = 1280 * 1024


c = 0

print("Content-type: text/html")
print()

for i in owner_id:
	if (i.text[0] == '-'): #теперь можно переходить по ссылке на пост (а не только на страницу человека)
		VkUrl = 'https://vk.com/photo' + i.text + '_' + pid[c].text
	else:
		VkUrl = 'https://vk.com/id' + i.text

	print('<a href="' + VkUrl + '">' +	 VkUrl + '</a><br>')
	ImgUrl = src_big[c].text
	if ((int(width[c].text) * int(height[c].text)) > size_xxbig):
		print('<a href="' + src_xxxbig[c].text + '">')
	else:
		if((int(width[c].text) * int(height[c].text)) > size_xbig):
			print('<a href="' + src_xxbig[c].text + '">')
		else:
			if((int(width[c].text) * int(height[c].text)) > size_big):
				print('<a href="' + src_xbig[c].text + '">')	
			else:
				print('<a href="' + src_big[c].text + '">')	
	print('<img src="' + src_big[c].text + '">') #Нужно решить проблему с переходом на более большую версию фотографии(переходит не на ту фотографию)
	print('</a><br>')
	print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(int(created[c].text))) + '<br>')
	print(lat[c].text + '<br>')
	print(_long[c].text + '<br>')
	c += 1
	print('<br>')




