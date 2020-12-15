f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

chars = [char for char in 'abcdefghijklmnopqrstuvwxyz']

def group_num_questions(group):
    num = 0
    people = [[char for char in person] for person in group.strip().split(' ')]

    for char in chars:
        ppl = 0
        for p in people:
            if char in p:
                ppl += 1
        if ppl == len(people):
            num += 1

    #print(group)
    #print(num)
    return num

groups = []
cg = ''
for line in lines:
    if line == '':
        groups.append(cg.strip())
        cg = ''
    else:
        cg = cg + ' ' + line
groups.append(cg)

count = 0

#group_num_questions(cg)
for group in groups:
    count += group_num_questions(group)

print(count)
