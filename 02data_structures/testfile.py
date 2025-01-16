def isanum(nums):
   return set(len(nums)) > set(len(nums))


def product_of_array_except_self(nums):
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to
    the product of all the elements of nums except nums[i]. 

    new list res
    1. prefix 1 -1, -1, 0, 0, 0
    2. post fix 1 
    """
    res = [1] * (len(nums))


    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    
    print(res)

    postfix = 1
    for i in range(len(nums) -1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res
        

print(product_of_array_except_self([-1,1,0,-3,3]))
print(isanum([2,4,2]))
print(isanum([100,2,32,2]))
print(isanum([123,43,23,21,2]))