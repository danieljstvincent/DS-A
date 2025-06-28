"""
solution 1 | Sorting | O(n log n)


Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
                     |, 
            {1, 2, 3}

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true




"""
def containsDuplicateBruteForce(nums):
    
      
      return True


def containsDuplicate(nums):
        seen = set()
        
        for num in nums:
            print(seen)
            if num in seen:
                    return True
            seen.add(num)
        return False

print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print(containsDuplicate([1,4,5,1]))
print(containsDuplicate([1,2,3,4]))

