# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
#inp = fh.read();
#inp_upper = inp.upper()
#print inp_upper
for line in fh:
    line2 = line.strip()
    line3 = line2.upper()
    print line3