
def twoSum(nums,target):
    index_tool = {}

    for i, num in enumerate(nums):
        if target - num in index_tool:
            return [i, index_tool[target - num]]
        index_tool[num] = i
       


print(twoSum([2,7,11,15], 9 ))
 #            0 1 2  3
 #            9 - num in {}
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6 ))