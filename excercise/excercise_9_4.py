name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
email = list()
for line in handle:
    line = line.rstrip()
    words = line.split()
    if len(words)<1: continue
    if words[0] != 'From': continue
    email.append(words[1])
#print email

emaildic = dict()
for eee in email:
    emaildic[eee] = emaildic.get(eee,0)+1
#print emaildic

maxEmail = None
maxCount = None
for kkk, vvv in emaildic.items():
    if maxEmail is None or maxCount < emaildic[kkk]:
        maxEmail = kkk
        maxCount = vvv    
print maxEmail, maxCount        