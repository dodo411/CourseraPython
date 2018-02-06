name = raw_input("Enter file:")
if len(name) < 1 : name = "regex_sum_338794.txt"

import re
handle = open(name)
num_list = list();
for line in handle:
    line = line.rstrip()
    num = re.findall('[0-9]+',line)
    if num == []: continue
#    print line
    for i in num:
        num_list.append(int(i))
#    print num
#    print num_list

print name
print 'sum =', sum(num_list)

print 'single line sum:'
print sum( [ int(i) for i in re.findall('[0-9]+',open('regex_sum_338794.txt').read()) ] )
