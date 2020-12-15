import math

f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

seat_map = [[seat for seat in row]for row in lines]
seat_map.insert(0,['-' for seat in lines[0]])
seat_map.append(['-' for seat in lines[0]])
s_dirs = [[1,0],[1,1],[1,-1],[0,1],[0,-1],[-1,0],[-1,1],[-1,-1]]

for row in seat_map:
    row.insert(0,'-')
    row.append('-')

def apply_rules(map):
    new_map = [row.copy() for row in map]
    for y in range(1,len(map)-1):
        for x in range(1,len(map[y])-1):
            seen_seats = []
            for dir in s_dirs:
                seen = False
                amt = 1
                while seen == False:
                    row = y+dir[0]*amt
                    col = x+dir[1]*amt
                    char =  map[row][col]
                    if char != '.':
                        seen = True
                        seen_seats.append(char)
                    amt += 1
            #if x == 1 and y == 1:
                #print(seen_seats)

            if map[y][x] == 'L' and seen_seats.count('#') == 0:
                new_map[y][x] = '#'
            elif map[y][x] == '#' and seen_seats.count('#') >= 5:
                new_map[y][x] = 'L'
    return new_map

m = []
while m != seat_map:
    m = seat_map
    seat_map = apply_rules(seat_map)
#seat_map =apply_rules(seat_map)
count_occupied = 0
for row in seat_map:
    #print(row)
    for seat in row:
        if seat == '#':
            count_occupied += 1

print(count_occupied)
