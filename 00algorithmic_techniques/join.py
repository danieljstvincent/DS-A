"""
Does 3 O(n)
1. in-place swapping elements in a list
2. in-place swap elements in the original array.
3. Add a extra space for ever 0 in the array withnout excited the size of the original array


"""

def quesion1(nums):
    pass

def quesion2(nums):
    pass

def quesion3(nums):
   #
   i = 0
   while i < len(arr) -1:
       if arr[i] == 0:
           arr.insert(i+1, 0)
           del arr[len(arr)-1]
           i = i + 2
           return i
 

print(quesion1([1,0,2,3,0,4,5,0]):
print(quesion2([1,0,2,3,0,4,5,0]):
print(quesion3([1,0,2,3,0,4,5,0]):