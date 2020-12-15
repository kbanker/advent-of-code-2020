f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

nums = [int(line) for line in lines]
nums.sort()
#nums.insert(0,0)

def check(arr):
    for i in range(1,len(arr)):
        if arr[i] - arr[i-1] > 3:
            return False
    return True

combinations = {0:1}
for num in nums:
    combinations[num] = 0
    combinations[num] += combinations.get(num-1,0)
    combinations[num] += combinations.get(num-2,0)
    combinations[num] += combinations.get(num-3,0)

print(combinations[nums[-1]])
