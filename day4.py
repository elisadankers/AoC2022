data = open('input4.txt','r').read().strip().split('\n')

part1 = 0
part2 = 0
for line in data:
    elf1, elf2 = line.split(',')
    elf1_start, elf1_end = elf1.split('-')
    elf2_start, elf2_end = elf2.split('-')

    #part 1
    if (int(elf1_start) <= int(elf2_start) and int(elf1_end) >= int(elf2_end)) \
    or (int(elf2_start) <= int(elf1_start) and int(elf2_end) >= int(elf1_end)): 
        part1 += 1        
    
    #part 2
    if (int(elf2_start) <= int(elf1_end))and (int(elf2_end) >= int(elf1_start)):
        part2 += 1

print(part1)
print(part2)
