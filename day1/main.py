f = open('input.txt')
nums= [eval(x) for x in f]
f.close()

for num in nums:
    num = int(num)
    for x in nums:
        x = int(x)
        for y in nums:
            if y + x + num == 2020:
                print(num * x*y)
                break
