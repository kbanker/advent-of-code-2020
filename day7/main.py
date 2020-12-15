f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

bags = {}
bags_c = {} # 1 contain, 0 idk, -1 dont
visited = {}
for line in lines:
    words = line.split(' ')
    bag = words[0] + words[1]
    contents = []
    i = 4
    for word in words[4:]:
        if word[:3] == 'bag' and words[i-2] != 'no':
             contents.append((int(words[i-3]),words[i-2] + words[i-1]))
             #contents.append(words[i-2] + words[i-1])

        i += 1

    bags[bag] = contents
    visited[bag] = False
    bags_c[bag] = False

def search(bag):
    contents = bags[bag]
    visited[bag] = True
    if contents == []:
        return False
    elif 'shinygold' in contents:
        return True
    else:
        for c in contents:
            if search(c):
                return True

        return False

def search2(bag):
    contents = bags[bag]
    if contents == []:
        return 0
    else:
        count = 0
        for bag in contents:
            count += bag[0] + bag[0]*search2(bag[1])
        return count

#for bag, contents in bags.items():
#    bags_c[bag] = search(bag)
    #print(bag)

count = 0
#for bag, c in bags_c.items():
#    if c:
#        count += 1

print(search2('shinygold'))
