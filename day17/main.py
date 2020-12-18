import math

f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()



active = {}

for x in range(len(lines)):
    for y in range(len(lines[0])):
        if lines[x][y] == '#':
            active[(x,y,0,0)] = lines[x][y]

def apply_rules(current):
    final = {}
    inactive = {}# amount of active neighbors
    for pos in current.keys():
        neighbors = [[[[(x,y,z,w) for x in range(pos[0]-1, pos[0]+2)] for y in range(pos[1]-1, pos[1]+2)]for z in range(pos[2]-1, pos[2]+2)] for w in range(pos[3]-1,pos[3]+2)]
        neighbors[1][1][1].remove(pos)

        n_states = []

        for dim in neighbors:
            for plane in dim:
                for row in plane:
                    for cube in row:
                        state = current.get(cube, '.')
                        n_states.append(state)

                        if state == '.':
                            inactive[cube] = inactive.get(cube, 0) + 1

                            if inactive[cube] == 3:
                                final[cube] = '#'
                            elif inactive[cube] > 3:
                                final[cube] = '.'

        active_neighbors = n_states.count('#')

        if active_neighbors == 2 or active_neighbors == 3:
            pass
        else:
            final[pos] = '.'
            #if pos == (2,0,0): print(n_states)

    current.update(final)
    final = {k:v for (k,v) in current.items() if v == '#'}
    return final

def p_plane(dict, z):
    c=0
    plane = [['.' for i in range(5)]for z in range(5)]
    for k, v in dict.items():
        if k[2] ==z:
            plane[k[0]][k[1]] = v
            c+=1
    #print(c)
    for row in plane: print(row)

#print(active)
#p_plane(active,0)
for i in range(6):
    active = apply_rules(active)
#print(active)
print(len(active))

#p_plane(active,0)
