f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

def check(cmds):
    visited = {}
    index = 0
    acc = 0
    for i in range(len(cmds)):
        if visited.get(index, False):
            return False
        elif len(cmds) <= index:
            return acc

        visited[index] = True
        words = cmds[index].split(' ')
        cmd = words[0]
        num = int(words[1])
        #print(num)
        if cmd == 'acc':
            acc += num
            index += 1
        elif cmd == 'jmp':
            index += num
        else:
            index += 1

test = []
for i in range(len(lines)):
    test = lines.copy()
    words = lines[i].split(' ')
    chk = False
    if words[0] == 'nop':
        test[i] = 'jmp ' + words[1]
        chk = True
    elif words[0] == 'jmp':
        test[i] = 'nop ' + words[1]
        chk = True

    if chk:
        if check(test) != False:
            print(check(test))


#print(test)
