# 1. Iterate Over an Array
# Write a function that prints each element in an array in order from the first to the last.

# 2. Iterate Over an Array in Reverse
# Modify the previous function to print the elements in reverse order, from the last to the first.

# 3. Fetch Every Second Element
# Write a function that accesses every other element in the array, starting from the first element.

# 4. Find the Index of a Target Element
# Write a function that searches for a specific element in an array and returns its index. If the element is not found, return -1.

# 5. Find the First Prime Number in an Array
# Iterate over an array and find the first prime number. Stop the iteration once you find it.

# 6. Traverse a Two-Dimensional Array
# Write a function to print all elements of a 2D array (matrix), row by row.

# 7. Traverse the Main Diagonal of a Matrix
# Print the elements along the main diagonal of a square matrix, where the row and column indices are equal.

# 8. Traverse the Perimeter of a Matrix
# Print the elements along the outer edge (perimeter) of a 2D array.

# 9. Traverse Elements in Spiral Order
# Print elements of a 2D array in spiral order, starting from the top-left corner and moving inward.

# 10. Traverse the Lower Triangle of a Matrix
# Print the elements below and including the main diagonal of a square matrix.

# 11. Calculate the Sum of an Array
# Write a function that calculates the sum of all elements in an array by accumulating the total as you iterate.

# 12. Find the Minimum and Maximum Elements
# Find the smallest and largest numbers in an array by updating minimum and maximum variables during iteration.

# 13. Find the Indices of the Min and Max Elements
# In addition to finding the min and max values, keep track of their positions (indices) in the array.

# 14. Find the Two Smallest/Largest Elements Without Sorting
# Modify your approach to keep track of the two smallest and two largest elements during a single pass through the array.

# 15. Count Occurrences of a Specific Element
# Count how many times a given element appears in the array by incrementing a counter whenever you encounter it.

# 16. Count Occurrences of All Elements
# Use a dictionary or map to count the number of times each unique element appears in the array during a single iteration.

# 17. Find the Two Most Frequent Elements
# Find the two elements that appear the most number of times in an array.

# 18. Compute Prefix Sums
# Create an array where each element at index i is the sum of all elements up to that index in the original array. We call this array prefix sums array.

# 19. Find the Sum of Elements in a Given Range
# Given a range (start and end indices), write a function that calculates the sum of elements within that range by iterating from the start to the end index and accumulating the sum.

# 20. Efficient Range Sum Queries Using Prefix Sums
# After computing the prefix sums array, answer multiple range sum queries efficiently:
# Instead of summing elements for each query, use the prefix sums array to compute the sum of elements between indices i and j in constant time.
# Hint: The sum from index i to j can be calculated as prefix_sum[j] - prefix_sum[i - 1]. This method requires understanding how to manipulate indices and handle edge cases when i is 0.

# 21. Calculate the nth Fibonacci Number
# Write a recursive function to find the nth Fibonacci number, where each number is the sum of the two preceding ones.

# 22. Sum of an Array Using Recursion
# Find the sum of all elements in an array by recursively summing the first element and the sum of the rest of the array.

# 23. Find the Minimum Element in an Array Using Recursion
# Find the smallest element in an array without using loops by comparing the first element with the minimum of the rest of the array.

# 24. Reverse a String Using Recursion
# Reverse a given string by recursively swapping characters from the ends towards the center.

# 25. Check if a String is a Palindrome Using Recursion
# Determine if a string reads the same backward as forward by comparing characters from the outside in.

# 26. Generate All Permutations of a String
# Recursively generate all permutations of the characters in a string by swapping characters.

# 27. Generate All Subsets of a Set
# Generate all possible subsets (the power set) of a set of numbers by including or excluding each element recursively.

# 28. Compute the Sum of Digits of a Number
# Given an integer, write a recursive function to compute the sum of its digits.

# 29. Compute the Power of a Number
# Write a recursive function to compute x raised to the power n (i.e., compute x^n), where n is a non-negative integer.

# 30. Count the Number of Occurrences of a Character in a String Using Recursion
# Write a recursive function to count how many times a specific character appears in a string.



# Iterate Over an Array
def iterateOverAnArray(nums):
    return [num for num in nums]

# Iterate Over an Array in Reverse
#solution 1: return [num for num in reversed(nums)] O(n) Space O(n) because a new list in create
#solution 2: return [nums[::-1]] Time: O(n) Space O(n) because a new list in create, but general fast as it works in c=
def iterateOverAnArrayinReverse(nums):
    return nums[::-1]
        

# Fetch Every Second Element
def EverySecondElement(nums):
    return nums[::2]

# Find the Index of a Target Element
def indexOfTarget(nums, target):
    for value, index in enumerate(nums):
        if value == target:
            return index
    return -1

# 5. Find the First Prime Number in an Array
"""
generator expression with next() to find the first prime number in num

"""
def FindThePrimenums(nums):
    return next((num for num in nums if all(num % i != 0 for i in range(2, int(num**0.5) + 1)) and num > 1), None)

# 6. Traverse a Two-Dimensional Arraysdf
def print_matrix(matrix):
    total = []
    for row in matrix:
        for element in row:
            print(element, end= " ")
    print(element)


# 7 Traverse the Main Diagonal of a Matrixc
def main_diagonal(matrix):

    range_and_len_matrix, range_matrix, len_matrix = [],[],[]

    for i in range(len(matrix)):
        range_and_len_matrix.append(i)
        for j in range(matrix[i][i]):
            range_matrix.append(j)
            for l in len(matrix):
                len_matrix.append(l)
            print( i, j, l)
        print()
   
    #return [matrix[i][i] for i in range(len(matrix))]

# Traverse the Perimeter of a Matrix
def perimeter(matrix):
    n = len(matrix)
    return matrix[0] + [row[-1] for row in matrix[1:-1]] + matrix[-1][::-1] + [row[0] for row in matrix[-2:0:-1]]

# Traverse Elements in Spiral Order
def spiral_order(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)  # top row
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())  # right column
        if matrix:
            result += matrix.pop()[::-1]  # bottom row reversed
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))  # left column
    return result

# Traverse the Lower Triangle of a Matrix
def lower_triangle(matrix):
    return [matrix[i][:i+1] for i in range(len(matrix))]

# Calculate the Sum of an Array
def sum_array(arr):
    return sum(arr)

# Find the Minimum and Maximum Elements
def min_max(arr):
    return min(arr), max(arr)

# Find the Indices of the Min and Max Elements
def min_max_indices(arr):
    min_val, max_val = min(arr), max(arr)
    return arr.index(min_val), arr.index(max_val)

# Find the Two Smallest/Largest Elements Without Sorting
import heapq
def two_smallest_largest(arr):
    return heapq.nsmallest(2, arr) + heapq.nlargest(2, arr)
    """
        smallest, largest = float('inf'), float('-inf')
    second_smallest, second_largest = float('inf'), float('-inf')
    for num in arr:
        if num < smallest:
            second_smallest, smallest = smallest, num
        elif num < second_smallest:
            second_smallest = num
        if num > largest:
            second_largest, largest = largest, num
        elif num > second_largest:
            second_largest = num
    return second_smallest, smallest, second_largest, largest
    """


# Count Occurrences of a Specific Element
def count_occurrences(arr, element):
    return arr.count(element)

# Count Occurrences of All Elements
def count_all_occurrences(arr):
    return {element: arr.count(element) for element in set(arr)}

# Find the Two Most Frequent Elements
from collections import Counter
def two_most_frequent(arr):
    return [item[0] for item in Counter(arr).most_common(2)]

# Compute Prefix Sums
def prefix_sums(arr):
    return [sum(arr[:i+1]) for i in range(len(arr))]

# Find the Sum of Elements in a Given Range
def sum_range(arr, start, end):
    return sum(arr[start:end+1])

# Efficient Range Sum Queries Using Prefix Sums
def efficient_range_sum(prefix_sums, start, end):
    return prefix_sums[end] - (prefix_sums[start - 1] if start > 0 else 0)

# Calculate the nth Fibonacci Number


def fibonacci(n):
    #memoizaion
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
"""
    recuisive
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)
"""


# Sum of an Array Using Recursion
def sum_array_recursive(arr):
    return arr[0] + sum_array_recursive(arr[1:]) if arr else 0

# Find the Minimum Element in an Array Using Recursion
def min_element(arr):
    return arr[0] if len(arr) == 1 else min(arr[0], min_element(arr[1:]))

# Reverse a String Using Recursion
def reverse_string(s):
    return s if len(s) == 0 else reverse_string(s[1:]) + s[0]

# Check if a String is a Palindrome Using Recursion
def is_palindrome(s):
    return s == s[::-1] if len(s) <= 1 else s[0] == s[-1] and is_palindrome(s[1:-1])

# Generate All Permutations of a String
def permutations(s):
    return [s] if len(s) == 1 else [s[i] + p for i in range(len(s)) for p in permutations(s[:i] + s[i+1:])]

# Generate All Subsets of a Set
def subsets(s):
    return [s] if not s else subsets(s[1:]) + [s[:1] + item for item in subsets(s[1:])]

# Compute the Sum of Digits of a Number
def sum_digits(n):
    return n if n < 10 else n % 10 + sum_digits(n // 10)

# Compute the Power of a Number
def power(x, n):
    return x ** n

# Count the Number of Occurrences of a Character in a String Using Recursion
"""
s = "hello" | c = l
     return 1 + count_char(s[1:], char) if s and s[0] == char else (0 if not s else count_char(s[1:], char))  
"""
def count_char(s, char):
    return 1 + count_char(s[1:], char)if s and s[0] == char else (0 if not s else count_char(s[1:], char))

# Test Cases
print(iterateOverAnArray([12, 54, 32, 100.1]), "Q1-iterateOverAnArray")
print(iterateOverAnArrayinReverse([12, 54, 32, 100.1]), "Q2-iterateOverAnArrayinReverse")
print(EverySecondElement([12, 54, 32, 100.1]), "Q3-EverySecondElement")
print(indexOfTarget([12, 54, 32, 100.1], 32), "Q4-indexOfTarget")
print(FindThePrimenums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), "Q5-FindThePrimenums")
print(print_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), "Q6-print_matrix")
print(main_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), "Q7-main_diagonal")
print(perimeter([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), "Q8-perimeter")
print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), "Q9-spiral_order")
print(lower_triangle([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), "Q10-lower_triangle")
print(sum_array([1, 2, 3, 4]), "Q11-sum_array")
print(min_max([1, 2, 3, 4]), "Q12-min_max")
print(min_max_indices([1, 2, 3, 4]), "Q13-min_max_indices")
print(two_smallest_largest([1, 2, 3, 4]), "Q14-two_smallest_largest")
print(count_occurrences([1, 2, 3, 4, 2], 2), "Q15-count_occurrences")
print(count_all_occurrences([1, 2, 3, 4, 2]), "Q16-count_all_occurrences")
print(two_most_frequent([1, 2, 3, 2, 2, 3]), "Q17-two_most_frequent")
print(prefix_sums([1, 2, 3, 4]), "Q18-prefix_sums")
print(sum_range([1, 2, 3, 4], 1, 2), "Q19-sum_range")
print(fibonacci(5), "Q20-fibonacci")
print(sum_array_recursive([1, 2, 3, 4]), "Q21-sum_array_recursive")
print(min_element([4, 1, 7, 3]), "Q22-min_element")
print(reverse_string("hello"), "Q23-reverse_string")
print(is_palindrome("racecar"), "Q24-is_palindrome")
print(permutations("abc"), "Q25-permutations")
print(subsets([1, 2, 3]), "Q26-subsets")
print(sum_digits(1234), "Q27-sum_digits")
print(power(2, 3), "Q28-power")
print(FindThePrimenums([1, 4, 6, 8, 10, 3, 7]), "Q29-FindThePrimenumsr")  # Output: 3
print(count_char("hello", "l"), "Q30-count_char")




