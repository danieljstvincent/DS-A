"""
https://leetcode.com/problems/shuffle-the-array/
"""
def shuffle( nums,n):
    solution = []
    midpoint = len(nums) // 2

    leftside = nums[:midpoint]
    rightside = nums[midpoint:]

    
    for i in range(n):
        solution.append(leftside[i])
        solution.append(rightside[i])
        
    if nums[-1] not in solution:
        solution.append(nums[-1])

    return solution


print(shuffle([2,5,1,3,4,7,8], 3))
        