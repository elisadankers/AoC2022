data = open('input2.txt','r').read().strip().split('\n')

score = 0
score2 = 0
rock = 0
paper = 0
scissors = 0

for line in data:
    opponent, me = line.split(' ')
    #part 1
    if (opponent == 'A' and me == 'X') or (opponent == 'B' and me == 'Y') or (opponent == 'C' and me == 'Z'):
        score += 3
    elif (opponent == 'A' and me == 'Y') or (opponent == 'B' and me == 'Z') or (opponent == 'C' and me == 'X'):
        score += 6

    #part 2
    if (opponent == 'A' and me == 'X'):
        scissors += 1
    elif (opponent == 'A' and me == 'Y'):
        rock += 1
    elif (opponent == 'A' and me == 'Z'):
        paper += 1
    elif (opponent == 'B' and me == 'X'):
        rock += 1
    elif (opponent == 'B' and me == 'Y'):
        paper += 1
    elif (opponent == 'B' and me == 'Z'):
        scissors += 1
    elif (opponent == 'C' and me == 'X'):
        paper += 1
    elif (opponent == 'C' and me == 'Y'):
        scissors += 1
    elif (opponent == 'C' and me == 'Z'):
        rock += 1

    if me == 'X':
        score += 1
    elif me == 'Y':
        score += 2
        score2 += 3
    else:
        score += 3
        score2 += 6

#answer 1
print(score)
#answer 2
print(score2 + rock + 2*paper + 3*scissors)
