f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

nums = [int(line) for line in lines]

def invalid_num():
    for i in range(25,len(nums)):
        num =  nums[i]
        isValid = False
        for x in nums[i-25:i]:
            for y in nums[i-25:i]:
                if x is not y and x+y == num:
                    isValid = True
        if not isValid:
            return (num,i)


inv_num, ind = invalid_num()

def find_set():
    test = []
    sum = 0
    for i in range(len(nums)):
        test.clear()
        sum = 0
        for x in range(i,len(nums)):
            test.append(nums[x])
            sum += nums[x]
            if sum > inv_num:
                #print('b')
                break
            elif sum == inv_num:
                print(sum)
                return test
    return test

ans = find_set()
ans.sort()

print(ans[0] + ans[-1])
