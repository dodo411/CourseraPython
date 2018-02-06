fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    content = line.split()
#    print content
    for ww in content:
        if lst == []: 
            lst.append(ww)
#            print lst
        if ww in lst: continue
        lst.append(ww)
lst.sort()
print lst