import re
import copy

stacks, commands = open('input5.txt','r').read().split('\n\n')

*stacks, indices = stacks.splitlines()

stack = [[],[],[],[],[],[],[],[],[]]
commands = list(map(int,re.findall(r'\d+',commands)))

for line in stacks[::-1]:
    [stack[ci].append(c) for ci,c in enumerate(line[1::4]) if c != ' ']

stack1, stack2 = copy.deepcopy(stack), copy.deepcopy(stack)

for i in range(0,len(commands),3):
    for n in range(commands[i]):
        x = stack1[commands[i+1]-1].pop()
        stack1[commands[i+2]-1].append(x)

part1 = str()
for i in range(9):
    part1 += stack1[i][-1]

print(part1)


for i in range(0,len(commands),3):
    x = stack2[commands[i+1]-1][-commands[i]:]
    stack2[commands[i+1]-1] = stack2[commands[i+1]-1][:-commands[i]]
    stack2[commands[i+2]-1] += x
    
part2 = str()
for i in range(9):
    part2 += stack2[i][-1]

print(part2)