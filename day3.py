import re

data = open('input3.txt','r').read().strip().split('\n')

pattern_lower = r'[a-z]'

#Part 1
total = 0
for line in data:
    compartment1 = line[:int(len(line)/2)]
    compartment2 = line[int(len(line)/2):]
    for item in compartment1:
        if item in compartment2:
            double_item = item

    if re.match(pattern_lower,double_item):
        priority = ord(double_item) - 96
    else:
        priority = ord(double_item) - 38
    
    total += priority

print(total)

#Part 2
total_badge = 0
for i in range(0,len(data),3):
    for n in data[i]:
        if n in data[i+1] and n in data[i+2]:
            badge = n
    if re.match(pattern_lower,badge):
        priority_badge = ord(badge) - 96
    else:
        priority_badge = ord(badge) - 38
    
    total_badge += priority_badge

print(total_badge)