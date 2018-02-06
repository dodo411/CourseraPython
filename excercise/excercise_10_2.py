name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hrdict = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    if len(words)<7: continue
    if words[0]!='From': continue
    tt = words[5].split(':')
    hrdict[tt[0]] = hrdict.get(tt[0],0) + 1

#print hrdict


for k in sorted(hrdict):
    print k,hrdict[k]
    
