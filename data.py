from BeautifulSoup import BeautifulSoup
import urllib2
import re

html_page = urllib2.urlopen("http://imgur.com")
soup = BeautifulSoup(html_page)
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))

print(images)
