import json
import urllib


#url = "http://python-data.dr-chuck.net/comments_42.json"
url = "http://python-data.dr-chuck.net/comments_338800.json"
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print "Retriving", len(data), "characteres"  
info = json.loads(str(data)) # info is a list
#print type(info)
info2 = info.values()[1]
print 'User count:', len(info2)

total = 0
for item in info2:
#    print type(item)
#    print 'Name', item['name']
#    print 'Count', item['count']
    total = total+int(item['count'])
print "Total: ", total

