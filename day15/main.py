import math

f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

start_nums = [int(x) for x in lines[0].split(',')]
nums = {}
for i in range(len(start_nums)-1):
    nums[start_nums[i]] = i+1  #number, turn

last_num = start_nums[-1]
for i in range(len(start_nums) + 1,30000001):
    x = nums.get(last_num, 0)
    nums[last_num] = i - 1
    if x != 0:
        last_num = i - x - 1
    else:
        last_num = 0

print(last_num)
#print(len(nums))
