# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL - ')
if len(url) < 1 : url = "http://python-data.dr-chuck.net/known_by_Jaina.html"
count = raw_input('Enter count: ')
if len(count) < 1 : 
    count = 4
else:
    count = int(count)

position = raw_input('Enter position: ')
if len(position) < 1 : 
    position = 3
else:
    position = int(position)

while count > 0:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    # Retrieve all of the anchor tags
    tags = soup('a')
    tag = tags[position-1]
    url = tag.get('href', None)
    print url
    count = count-1
    
lastname = url.split('_by_')[1]
#print lastname
lastname = lastname.split('.')[0]
print lastname
#for tag in tags:
#    print tag.get('href', None)
