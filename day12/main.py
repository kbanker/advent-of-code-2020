import math

f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

dirs = [(line[0], int(line[1:])) for line in lines]
c_dir = [1,0] # current dir
pos = [0,0]
w_pos = [10,1]

for dir, val in dirs:
    if dir == 'N':
        w_pos[1] += val
    elif dir == 'S':
        w_pos[1] -= val
    elif dir == 'E':
        w_pos[0] += val
    elif dir == 'W':
        w_pos[0] -= val
    elif dir == 'F':
        pos[0] += w_pos[0]*val
        pos[1] += w_pos[1]*val
    elif dir == 'R' or dir == 'L':
        if dir == 'R':
            ang = -math.radians(val)
        else:
            ang = math.radians(val)
        n_dir = [0,0]
        n_dir[0] = round(w_pos[0]*math.cos(ang) - w_pos[1]*math.sin(ang))
        n_dir[1] = round(w_pos[0]*math.sin(ang) + w_pos[1]*math.cos(ang))
        w_pos = n_dir


#print(pos)
print(w_pos)
print(abs(pos[0])+abs(pos[1]))
