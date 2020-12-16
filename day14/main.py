import math
from bitstring import BitArray

f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

cmds = [(l.split(' ')[0],l.split(' ')[2]) for l in lines]

def into_mask(mask_str):
    m = {}
    for i in range(len(mask_str)):
        if mask_str[i] == '1':
            m[i] = '0b' + mask_str[i]
        elif mask_str[i] == 'X':
            m[i] = 'X'

    return m

mask = into_mask('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
mem = {}
for cmd, val in cmds:
    if cmd == 'mask':
        mask = into_mask(val)
        #print(mask)
    elif cmd[:3] == 'mem':
        pos = int(cmd.split('[')[1][:-1])
        bits = BitArray(int=pos, length=36)
        possible = [bits]
        #print(possible)
        for key, num in mask.items():
            if num == 'X':
                added = []
                for p in possible:
                    o = p.copy()
                    z = p.copy()
                    o.overwrite('0b0', key)
                    z.overwrite('0b1', key)
                    added.extend([o,z])
                possible = added.copy()
            else:
                for p in possible:
                    p.overwrite(num, key)
        for p in possible:
            mem[p.uint] = int(val)

amt = 0
for num in mem.values():
    amt += num


print(amt)

#a = BitArray(int=0,length=36)
#print(a)
#a.overwrite('0b1',35)
#print(a)
