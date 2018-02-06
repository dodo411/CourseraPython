import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
if len(url) < 1 : url = "http://python-data.dr-chuck.net/comments_338796.xml"

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
#print data
tree = ET.fromstring(data)

counts = tree.findall('comments/comment')
#counts = tree.findall('.//count')
numsum = 0
for count in counts:
#    print count.find('name').text
    numsum = numsum + int(count.find('count').text)
    
print "Sum:", numsum

#print counts

#num = counts[0].find('count').text
#print num