f = open('input.txt')
lines = [x.split() for x in f]
f.close()

low = [int(x[0].split('-')[0])-1 for x in lines]
high = [int(x[0].split('-')[1]) -1 for x in lines]

letter = [x[1][0] for x in lines]

pwd = [x[2] for x in lines]

count = 0

for i in range(len(lines)):
    if pwd[i][low[i]] == letter[i] or pwd[i][high[i]] == letter[i]:
        if pwd[i][low[i]] == letter[i] and pwd[i][high[i]] == letter[i]:
            pass
        else:
            count += 1

print(count)
