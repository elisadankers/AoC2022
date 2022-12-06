import re

data = open('input6.txt','r').read()

#Part 1
part1 = 0
for i in range(len(data)-4):
    marker = r'[^'+ data[i+1:i+4]+']'
    if re.match(marker,data[i]):
        marker = r'[^'+ data[i+2:i+4]+']'
        if re.match(marker,data[i+1]):
            marker = r'[^'+data[i+3]+']'
            if re.match(marker,data[i+2]):
                part1 = i+4
                break
print(part1)

#Part 2
part2 = 0
count = 0
for i in range(len(data)-14):
    for n in range(14):
        marker = r'[^'+ data[i+n+1:i+15]+']'
        if re.match(marker,data[i+n]):
            count +=1
            print(count)
        else:
            count = 0
            continue
    if count == 13:
        part2 = i + 15
        break
    count = 0

print(part2)
