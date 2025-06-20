nums = [1, 2, 2]

def generateSubsets(start, subset):
    global nums
    result = subset
    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i-1]:
            continue
        subset.append(nums[i])
        generateSubsets(i+1, subset)
        subset.pop()

generateSubsets(1, [])
