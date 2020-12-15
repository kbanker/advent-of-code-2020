f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

#dH = 3 #amount horizontal: 3 right
#dV = 1 #amount vertical: 1 down
def count_trees(dH,dV):
    indH = dH
    indV = dV

    count = 0

    while indV < len(lines):
        if indH >= len(lines[0]):
            indH = (indH - len(lines[0]))
        if lines[indV][indH] == '#':
            count += 1
        #print(str(lines[indV][indH]) +' '+ str(indH))
        indH += dH
        indV += dV

    return count

print(count_trees(1,1)*count_trees(3,1) * count_trees(5,1)*count_trees(7,1)*count_trees(1,2))
