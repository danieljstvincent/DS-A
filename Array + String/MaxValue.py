# max valueWrite a function, max_value, that takes in list of numbers as an argument. The function should return the largest number in the list.
# Solve this without using any built-in list methods.
# You can assume that the list is non-empty.
# test_00

import math


# Value called max that stores the largest number in the Array
# If the next value is larger the prev value then that because the new Max
# float(-"inf")

def maxvalue(nums):
    max_num = float("-inf")
    for i in nums:
        if i > max_num:
            print(i, 'i',nums, 'nums', max_num, 'max_nums')
            max_num = i
    return max_num


    #     next_num = num[value] += 1
    # if next_num > max_num #store it
    #             max == next
    #     return mac


print(maxvalue([4, 7, 2, 8, 10, 9]))
max_value([-5, -2, -1, -11])