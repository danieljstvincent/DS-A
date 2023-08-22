

#count the letters in the first string then store it
#Count the numbers in the second string then store it.
#Compare the two amounts

def anagrams(nums1, nums2):
    # Remove spaces and convert to lowercase to ignore case and spaces
    nums1 = nums1.replace(" ", "")
    print(nums1, "nums1")
    nums2 = nums2.replace(" ", "")
    print(nums2, "nums2")
    # Check if the character counts are the same
    return sorted(nums1) == sorted(nums2)


print(anagrams('restful', 'fluster'))  # Output: True
print(anagrams('cats', 'tocs')) # -> False
print(anagrams('monkeyswrite', 'newyorktimes')) # -> True
print(anagrams('paper', 'reapa')) # -> False
print(anagrams('elbow', 'below')) # -> True
print(anagrams('tax', 'taxi')) # -> False
print(anagrams('taxi', 'tax')) # -> False
print(anagrams('night', 'thing')) # -> True
print(anagrams('abbc', 'aabc')) # -> False
print(anagrams('po', 'popp')) # -> false
print(anagrams('pp', 'oo')) # -> false
