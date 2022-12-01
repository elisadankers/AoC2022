data = open('input1.txt','r').read().split('\n\n')

max_calories = 0
item = []
top_three = [0, 0,0]
for elf in data:
    items = elf.split('\n')
    items = [int(n) for n in items]
    sum_calories = sum(items)
    if sum_calories > max_calories:
        max_calories = sum_calories
    if sum_calories > min(top_three):
        min_calories = top_three.index(min(top_three))
        top_three[min_calories] = sum_calories

print(max_calories)
print(sum(top_three))