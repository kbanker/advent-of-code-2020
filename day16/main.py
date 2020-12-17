f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

allowed_nums = []
allowed = {}
sec = 0
for line in lines[:lines.index('')]:
    cat = line.split(':')[0]
    allowed[cat] = []
    ranges = line.split(':')[1].split(' or ')
    for range_nums in ranges:
        nums = [x.strip().split('-') for x in range_nums.split(' or ')][0]
        allowed[cat].extend(range(int(nums[0]),int(nums[1])+1))
        allowed_nums.extend(range(int(nums[0]),int(nums[1])+1))

allowed_nums = set(allowed_nums)
tickets = []

for line in lines[lines.index('nearby tickets:')+1:]:
    valid = True
    vals = [int(x) for x in line.split(',')]
    for val in vals:
        if val not in allowed_nums:
            valid = False
    if valid:
        tickets.append(vals)

cols = [[] for x in range(len(allowed))]
for ticket in tickets:
    for pos in range(len(ticket)):
        cols[pos].append(ticket[pos])

#field_possibles = dict.fromkeys(allowed.keys(),[])
col_possibles = dict.fromkeys(range(len(cols)))
for col in cols:
    possible = []
    for key, nums in allowed.items():
        valid = True
        for val in col:
            if val not in nums:
                valid = False
                break
        if valid:
            possible.append(key)
            #print(key, cols.index(col))
    #for p in possible:
    #    field_possibles[p].append(cols.index(col))
    col_possibles[cols.index(col)] = possible

poss = list(allowed.keys())
ans = list(range(len(cols)))
for key in sorted(col_possibles, key=lambda x: len(col_possibles.get(x))):
    p = col_possibles[key]
    for x in p:
        if x in poss:
            poss.remove(x)
            ans[key] = x
            break
#print(ans)

my_ticket = [int(x) for x in lines[22].split(',')]

mult = 1
for i in range(len(ans)):
    a = ans[i]
    if a.startswith('departure'):
        mult *= my_ticket[i]
        print('x')

print(mult)
