import math

f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

ids = {}
i = 0
for char in lines[0].split(','):
    if char != 'x':
        ids[i] = int(char)
    i += 1

not_found = True
#print( %ids[0])
time = 0
step = 1
for pos, id in ids.items():
    while (time + pos) % id != 0:
        time += step
    step *= id


print(time)
