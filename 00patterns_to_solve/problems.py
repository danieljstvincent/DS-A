############################
# PROBLEM LIST (100 Problems)
############################
# 1. Print "Hello, World!" with a user-provided name.
# 2. Return the sum of two integers.
# 3. Given two numbers, return their sum, difference, product, and quotient.
# 4. Check if an integer is even.
# 5. Find the minimum and maximum of three numbers.
# 6. Count digits, letters, and spaces in a string.
# 7. Reverse a given string without built-in reverse functions.
# 8. Convert a string to uppercase, lowercase, and title case.
# 9. Check if a string is a palindrome.
# 10. Count the frequency of each character in a string.
# 11. Print the multiplication table of a given number.
# 12. Generate the first N Fibonacci numbers.
# 13. Compute the factorial of a number.
# 14. Check if a number is prime.
# 15. Compute the sum of digits of a number.
# 16. Reverse an integer’s digits.
# 17. Compute the average of a list of numbers.
# 18. Simple string compression: for "aaabbc", return "a3b2c1".
# 19. Sort a list of integers without using built-in sort.
# 20. Remove duplicates from a list.
# 21. Implement the Collatz sequence for a given integer.
# 22. Implement a Caesar cipher shift for a string.
# 23. Find the longest word in a sentence.
# 24. Rotate an array by a given number of steps.
# 25. Merge two sorted lists into one sorted list (no built-in sort).
# 26. Count vowels and consonants in a string.
# 27. Add two matrices.
# 28. Transpose a matrix.
# 29. Check if two strings are anagrams.
# 30. Find the GCD and LCM of two numbers.
# 31. Generate all permutations of a small set of characters.
# 32. Print the first N rows of Pascal’s triangle.
# 33. Convert a small integer to words (e.g., 0-999).
# 34. Remove stopwords from a sentence.
# 35. Print a histogram from a list of integers.
# 36. Run-length encode a string.
# 37. Check if parentheses/brackets are balanced.
# 38. Implement a sieve to find all primes up to N.
# 39. Check if one string is a rotation of another.
# 40. Print a 2D matrix in spiral order.
# 41. Validate Sudoku rows/columns partially.
# 42. Parse a CSV-like string and summarize data.
# 43. Justify text to a given width.
# 44. Convert infix expression to postfix (without direct stack usage).
# 45. Find a path in a maze using brute force (backtracking).
# 46. Normalize dates given in various formats.
# 47. Merge overlapping intervals.
# 48. Count inversions in a list (naive).
# 49. Find the longest common substring between two strings (naive).
# 50. Convert a numeric string to an integer manually.
# 51. Remove all occurrences of a substring from a string.
# 52. Count how many times a substring appears in a string.
# 53. Replace multiple spaces in a string with a single space.
# 54. Find the second largest number in a list.
# 55. Implement a basic command-line calculator (add, sub, mul, div).
# 56. Check if a number is a perfect number.
# 57. Generate a pattern of stars (e.g., pyramid, diamond).
# 58. Reverse the words in a sentence.
# 59. Given a list of words, remove duplicates while preserving order.
# 60. Check if a list is a palindrome.
# 61. Compute the nth harmonic number.
# 62. Find the median of a list of numbers.
# 63. Flatten a nested list.
# 64. Convert a number from decimal to binary.
# 65. Convert a number from binary to decimal.
# 66. Count the frequency of each word in a sentence.
# 67. Given a sentence, capitalize the first letter of each word.
# 68. Print a list of squares of numbers up to N.
# 69. Check if a year is a leap year.
# 70. Find the first non-repeating character in a string.
# 71. Compute compound interest for given principal, rate, and time.
# 72. Implement a basic unit conversion (e.g., Celsius to Fahrenheit).
# 73. Sum all even numbers in a list.
# 74. Sum all odd numbers in a list.
# 75. Remove all punctuation from a string.
# 76. Generate the prime factorization of a number.
# 77. Find the frequency of each digit in an integer.
# 78. Given a string, check if it consists of only unique characters.
# 79. Given a string, remove all digits.
# 80. Replace all occurrences of a character in a string with another character.
# 81. Given a list, rotate it until a certain element is at the front.
# 82. Given a sentence, reverse each word individually.
# 83. Find the index of the first occurrence of a given substring.
# 84. Implement a basic random password generator (deterministic for testing).
# 85. Check if two lists have the same elements in any order.
# 86. Given a list of dictionaries, filter them by a certain key-value.
# 87. Given a list of numbers, find the longest increasing subsequence (naive).
# 88. Count trailing zeros in factorial of a given number (naive).
# 89. Given a list of numbers, separate them into evens and odds.
# 90. Implement a basic "guess the number" logic (without I/O).
# 91. Compute the dot product of two vectors.
# 92. Implement a function that checks if a given string matches a simple regex (e.g., only '*', '?').
# 93. Shuffle a list of elements (deterministically for test).
# 94. Validate an email address format (simple checks).
# 95. Find the longest palindromic substring (naive).
# 96. Implement a simple Caesar cipher decoder.
# 97. Given a list of tuples (name, age), sort them by age without built-in sort.
# 98. Check if a number can be expressed as the sum of two squares.
# 99. Remove duplicate characters from a string.
# 100. Given a large number as a string, determine if it is divisible by 3.

############################
# FUNCTION TEMPLATES
############################
import fnmatch
import math
import random
import itertools

def problem_1(name: str):
    return f"Hello World, My name is {name}"

def problem_2(a: int, b: int):
    return a + b

def problem_3(a: float, b: float):
    """Return sum, difference, product, and quotient of two numbers."""
    total_sum = a + b
    total_subtract = a - b
    total_multiply = a * b
    total_divid = a % b
    return total_sum, total_subtract, total_multiply, total_divid
    

def problem_4(n: int):
    """Check if an integer is even."""
    return n % 2 == 0
  

def problem_5(a: int, b: int, c: int):
    """Find the minimum and maximum of three numbers."""
    mina = min(a, b, c)
    maxa = max(a, b, c)
    return mina,maxa

def problem_6(s: str):
    """Count digits, letters, and spaces in a string.
    s - "a c d"
    len(s) - 5
    range(len(0,1,2,3,4))

    my_list = ['a', 'b', 'c', 'd']
    for i in range(len(my_list)):
        print(f"Index {i}: {my_list[i]}")

    Index 0: a
    Index 1: b
    Index 2: c
    Index 3: d

    """
    return len(s)

def problem_7(s: str):
    """Reverse a string without built-in reverse.
    Solution 1:
    for i in range(len(s)) | On2
    """
    reversed_s = []
    reversed_chars = [s[i] for i in range(len(s)-1, -1, -1)]
    return ''.join(reversed_chars)

def problem_8(s: str):
    """Convert a string to uppercase, lowercase, and title case."""
    l = s.lower()
    u = s.upper()
    t = s.title()
    return l, u, t

def problem_9(s: str):
    """Check if a string is a palindrome."""
    reverse = s[::-1]
    return s == reverse

def problem_10(s: str):
    """Count frequency of each character in a string."""
    frequncey = {}
    for i in s:
        if i in frequncey:
            frequncey[i] += 1
        else:
            frequncey[i] = 1
    return frequncey
    

def problem_11(n: int):
    """Print the multiplication table of a number.
    range(12)
    num
    j += 1
    
    """
    list_of_multiplication = []
  
    for num in range(12):
        mulitiple = n * num
        list_of_multiplication.append(mulitiple)
        num += 1
    return list_of_multiplication

def problem_12(n: int):
    """Generate the first n Fibonacci numbers."""
    if n <= 0:
        return 0
    if n <=1:
        return 1
    return problem_12(n - 1) + problem_12(n - 2)

def problem_13(n: int):
    """Compute factorial of a number."""
    n = 5
    result = math.factorial(n)
    return result


def problem_14(n: int, k=5):
    """Check if a number is prime."""

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    def miller_test(d, n):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        while d != n - 1:
            x = (x * x) % n
            d *= 2
            if x == 1:
                return False
            if x == n - 1:
                return True
        return False
    
    d = n - 1
    while d % 2 == 0:
        d //= 2
    
    for _ in range(k):
        if not miller_test(d, n):
            return False
    return True

    

def problem_15(n: int):
    """Sum of digits of a number."""
    n_str = str(n)
    total = 0

    for num in n_str:
        total += int(num)
    return total

def problem_16(n: int):
    """Reverse digits of an integer."""
    reverse = ""
    
    pass

def problem_17(numbers: list):
    """Compute the average of a list of numbers."""

    pass

def problem_18(s: str):
    """Simple string compression."""
    pass

def problem_19(lst: list):
    """Sort a list without built-in sort.
    Bubble Sort Implementation
    """
    n = len(lst)

    for i in range(n):
        for j in range(0, n-i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + i] = lst[j + 1], lst[j]
    return n


def problem_20(lst: list):
    """Remove duplicates from a list."""
    new_lst = set(lst)
    return new_lst

def problem_21(n: int):
    """Implement the Collatz sequence."""
    pass

def problem_22(s: str, shift: int):
    """Caesar cipher shift."""
    pass

def problem_23(sentence: str):
    """Find the longest word in a sentence."""
    pass

def problem_24(lst: list, k: int):
    """Rotate an array by k steps."""
    pass

def problem_25(lst1: list, lst2: list):
    """Merge two sorted lists."""
    merged_list = []
    i = 0
    j = 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_list.append(lst1[i])
            i += 1
        else:
            merged_list.append(lst2[j])
            j += 1

    # append any remaining elements from lst1 or lst2
    merged_list.extend(lst1[i:])
    merged_list.extend(lst2[j:])

    return merged_list

def problem_26(s: str):
    """Count vowels and consonants."""
    vowels = "aeiou"
    vowel_count = 0
    consonants = 0

    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
               consonants += 1
    return {'Vowels':vowel_count, 'consonant': consonants}

def problem_27(m1: list, m2: list):
    """Add two matrices."""
    pass

def problem_28(matrix: list):
    """Transpose a matrix."""
    pass

def quick_sort(arr):
    """
    Sorts the input array using the Quick Sort algorithm.
    """
    if len(arr) < 2:
        return arr

    pivot = arr[len(arr) // 2]  # Choose a pivot element (here, the middle element)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

def problem_29(s1: str, s2: str) -> bool:
    """
    Check if two strings are anagrams using the quick_sort helper function.
    
    Args:
        s1 (str): The first string.
        s2 (str): The second string.
        
    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    # Step 1: Clean the strings (remove spaces and convert to lowercase)
    s1_clean = s1.replace(" ", "").lower()
    s2_clean = s2.replace(" ", "").lower()
    
    # Step 2: If the lengths of the two cleaned strings are different, they are not anagrams
    if len(s1_clean) != len(s2_clean):
        return False
    
    # Step 3: Sort both cleaned strings using the quick_sort() function
    sorted_s1 = quick_sort(list(s1_clean))
    sorted_s2 = quick_sort(list(s2_clean))
    
    # Step 4: Compare the sorted versions of the strings
    return sorted_s1 == sorted_s2

def problem_30(a: int, b: int):
    """Find GCD and LCM."""
    while b:
        a, b = b, a % b
    return a

def problem_31(chars: str):
    """Generate all permutations of given characters."""

    # Convert the input string to a list of characters for easier manipulation
    elements = list(chars)

    # Base case: if there's only one character, return it as the only permutation
    if len(elements) == 1:
        return [elements]

    perms = []
    # For each character, remove it from the list and generate permutations of the rest
    for i, elem in enumerate(elements):
        # The remaining characters after removing the current element 'elem'
        rest = elements[:i] + elements[i+1:]
        
        # Recursively call problem_31 on the remaining characters
        sub_perms = problem_31(''.join(rest))  # Convert rest back to string for the recursive call

        # Append the current element 'elem' in front of each of the permutations of the remaining characters
        for p in sub_perms:
            perms.append([elem] + p)

    return perms

def problem_32(n: int):
    """Print first n rows of Pascal’s triangle."""
    pass

def problem_33(n: int):
    """Convert integer to words (0-999)."""
    pass

def problem_34(sentence: str, stopwords: list):
    """Remove stopwords from sentence."""
    stopwords_set = set(stopwords)
    words = sentence.split()
    filter_word =[word for word in words if word not in stopwords_set]
    return ' '.join(filter_word)

def problem_35(lst: list):
    """Print a histogram from a list of integers."""
    pass

def problem_36(s: str):
    """Run-length encode a string."""
    pass

def problem_37(s: str):
    """Check if parentheses/brackets are balanced."""
    pass

def problem_38(n: int):
    """Sieve of Eratosthenes to find primes up to n."""
    pass

def problem_39(s1: str, s2: str):
    """Check if s2 is a rotation of s1."""
    pass

def problem_40(matrix: list):
    """Print matrix in spiral order."""
    pass

def problem_41(board: list):
    """Validate Sudoku rows/columns partially."""
    pass

def problem_42(csv_str: str):
    """Parse a CSV-like string and summarize data."""
    pass

def problem_43(words: list, width: int):
    """Justify text to given width."""
    pass

def problem_44(expression: str):
    """Convert infix to postfix."""
    pass

def problem_45(maze: list, start: tuple, end: tuple):
    """Find a path in a maze using brute force."""
    pass

def problem_46(date_str: str):
    """Normalize a date string."""
    pass

def problem_47(intervals: list):
    """Merge overlapping intervals."""
    pass

def problem_48(lst: list):
    """Count inversions in a list."""
    pass

def problem_49(s1: str, s2: str):
    """Longest common substring (naive)."""
    pass

def problem_50(num_str: str):
    """Convert numeric string to integer manually."""
    pass

def problem_51(s: str, sub: str):
    """Remove all occurrences of sub from s."""
    pass

def problem_52(s: str, sub: str):
    """Count how many times sub appears in s."""
    return s.count(sub)

def problem_53(s: str):
    """Replace multiple spaces in a string with a single space."""
    pass

def problem_54(lst: list):
    """Find the second largest number in a list."""
    pass

def problem_55(op: str, a: float, b: float):
    """Basic calculator for add, sub, mul, div."""
    pass

def problem_56(n: int):
    """Check if n is a perfect number."""
    pass

def problem_57(n: int):
    """Print a star pattern (e.g., pyramid) up to n rows."""
    pass

def problem_58(sentence: str):
    """Reverse the words in a sentence."""
    pass

def problem_59(words: list):
    """Remove duplicates from a list of words, preserving order."""
    pass

def problem_60(lst: list):
    """Check if a list is a palindrome."""
    reversed_lst = lst[::-1]
    return reversed_lst

def problem_61(n: int):
    """Compute the nth harmonic number."""
    if n < 1:
        return 0.0  # Or raise an error, depending on your needs
    
    harmonic_sum = 0.0
    for i in range(1, n + 1):
        harmonic_sum += 1.0 / i
    return harmonic_sum


def problem_62(lst: list):
    """Find the median of a list of numbers.
    - Sort the list
    - get the len of the list
    - get the mid of the list
    """
    if not lst:
        return None  # or raise an error, depending on your needs
    
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2

    if n % 2 == 1:
        # Odd number of elements -> single middle value
        return sorted_lst[mid]
    else:
        # Even number of elements -> average of two middle values
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2

def problem_63(nested_list: list):
    """Flatten a nested list."""
    flatten = list(itertools.chain.from_iterable(nested_list))
    return flatten

def problem_64(n: int):
    """Convert decimal to binary."""
    pass

def problem_65(b_str: str):
    """Convert binary to decimal."""
    pass

def problem_66(sentence: str):
    """Count frequency of each word in a sentence."""
    pass

def problem_67(sentence: str):
    """Capitalize the first letter of each word."""
    pass

def problem_68(n: int):
    """Print a list of squares of numbers up to n."""
    pass

def problem_69(year: int):
    """Check if a year is leap year."""
    pass

def problem_70(s: str):
    """Find first non-repeating character in a string."""
    pass

def problem_71(p: float, r: float, t: float):
    """Compute compound interest."""
    pass

def problem_72(celsius: float):
    """Convert Celsius to Fahrenheit."""
    pass

def problem_73(lst: list):
    """Sum all even numbers in a list."""
    pass

def problem_74(lst: list):
    """Sum all odd numbers in a list."""
    pass

def problem_75(s: str):
    """Remove all punctuation from a string."""
    pass

def problem_76(n: int):
    """Prime factorization of a number."""
    pass

def problem_77(n: int):
    """Frequency of each digit in an integer."""
    pass

def problem_78(s: str):
    """Check if a string has all unique characters."""
    pass

def problem_79(s: str):
    """Remove all digits from a string."""
    pass

def problem_80(s: str, old: str, new: str):
    """Replace all occurrences of old with new in s."""
    pass

def problem_81(lst: list, x):
    """Rotate a list until x is at the front."""
    pass

def problem_82(sentence: str):
    """Reverse each word in a sentence individually."""
    pass

def problem_83(s: str, sub: str):
    """Find the index of the first occurrence of sub in s."""
    pass

def problem_84(length: int):
    """Generate a deterministic 'random' password of given length."""
    pass

def problem_85(lst1: list, lst2: list):
    """Check if two lists have the same elements in any order."""

    pass

def problem_86(data: list, key: str, value):
    """Filter a list of dicts by key-value."""
    pass

def problem_87(lst: list):
    """Find the longest increasing subsequence (naive)."""
    pass

def problem_88(n: int):
    """Count trailing zeros in n! (factorial)."""
    pass

def problem_89(lst: list):
    """Separate even and odd numbers into two lists.
    """

    even_nums = []
    odd_nums = []

    for nums in lst:
        if nums % 2 == 0:
            even_nums += [nums]
        else:
            odd_nums += [nums]
    
    return even_nums, odd_nums

    

def problem_90(secret: int, guess: int):
    """Check guess against secret number (logic only)."""
    pass

def problem_91(vec1: list, vec2: list):
    """Compute the dot product of two vectors."""
    pass

def problem_92(s: str, pattern: str):
    """Simple pattern matching with '?' and '*'.

Solution 2:
def is_match(pattern: str, string: str) -> bool:
    s_len, p_len = len(string), len(pattern)
    i = j = 0  # i -> string pointer, j -> pattern pointer
    star_idx = -1  # position of the last '*'
    match_idx = 0  # position in the string that corresponds to the '*'

    while i < s_len:
        # Case 1: Current characters match, or pattern has '?'
        if j < p_len and (pattern[j] == string[i] or pattern[j] == '?'):
            i += 1
            j += 1
        # Case 2: '*' found, record its position and match from this point
        elif j < p_len and pattern[j] == '*':
            star_idx = j
            match_idx = i
            j += 1
        # Case 3: Last pattern character was '*', move to the next character in the string
        elif star_idx != -1:
            j = star_idx + 1
            match_idx += 1
            i = match_idx
        # Case 4: No match, and no available '*' to backtrack
        else:
            return False

    # Check if remaining characters in the pattern are all '*'
    while j < p_len and pattern[j] == '*':
        j += 1

    return j == p_len

    solution 3:

    def is_match(pattern: str, string: str) -> bool:
    m, n = len(pattern), len(string)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True  # Empty pattern matches empty string

    # Handle patterns like *, **, etc.
    for i in range(1, m + 1):
        if pattern[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[i - 1] == string[j - 1] or pattern[i - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[i - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return dp[m][n]

    """

    return fnmatch.fnmatch(s, pattern)

def problem_93(lst: list):
    """Shuffle a list deterministically."""
    pass

def problem_94(email: str):
    """Validate an email address format."""
    pass

def problem_95(s: str):
    """Find the longest palindromic substring (naive)."""
    pass

def problem_96(s: str, shift: int):
    """Caesar cipher decoder."""
    pass

def problem_97(tuples_list: list):
    """Sort list of (name, age) by age without built-in sort."""
    pass

def problem_98(n: int):
    """Check if a number can be expressed as sum of two squares."""
    pass

def problem_99(s: str):
    """Remove duplicate characters from a string."""
    removed_duplicate_char = set(s)
    return removed_duplicate_char



def problem_100(num_str: str):
    """Check if large number (string) is divisible by 3."""
    pass

############################
# TEST CALLS (3 test cases each)
############################

# For demonstration, we're just calling each function with sample parameters.
# In your own testing, you would print results or use assert statements.

print(problem_1("Alice"))
print(problem_1("Bob"))
print(problem_1("Charlie"))

print(problem_2(-1, 10))
print(problem_2(3, 4))
print(problem_2(0, 0))

print(problem_3(3.5, 2))
print(problem_3(-10, 2))
print(problem_3(10, 5))

print(problem_4(4))
print(problem_4(7))
print(problem_4(0))

print(problem_5(1, 2, 3),"problem5")
print(problem_5(10, 10, 5),"problem5")
print(problem_5(-1, -2, 0),"problem5")

print(problem_6("Hello 123"))
print(problem_6("No digits here!"))
print(problem_6("    "))

print(problem_7("abc"))
print(problem_7("Hello"))
print(problem_7("racecar"))

print(problem_8("hello world"))
print(problem_8("Test"))
print(problem_8("PYTHON"))

print(problem_9("racecar"))
print(problem_9("hello"))
print(problem_9(""))

print(problem_10("hello"))
print(problem_10("aabbcc"))
print(problem_10("xyz"))

print(problem_11(5))
print(problem_11(1))
print(problem_11(12))

print(problem_12(5), "problem_12")
print(problem_12(10), "problem_12")
print(problem_12(1), "problem_12")

print(problem_13(5))
print(problem_13(0))
print(problem_13(10))

print(problem_14(2))
print(problem_14(15))
print(problem_14(17))

print(problem_15(123))
print(problem_15(999))
print(problem_15(0))

print(problem_16(123))
print(problem_16(400))
print(problem_16(-123))

print(problem_17([1, 2, 3]))
print(problem_17([10, 20, 30]))
print(problem_17([5]))

print(problem_18("aaabbc"))
print(problem_18("aaaaa"))
print(problem_18("abc"))

print(problem_19([3, 2, 1]))
print(problem_19([10, 5, 5, 1]))
print(problem_19([1, 2, 3]))

print(problem_20([1, 2, 2, 3, 3]))
print(problem_20([4, 4, 4]))
print(problem_20([1]))

print(problem_21(6))
print(problem_21(19))
print(problem_21(1))

print(problem_22("abc", 1))
print(problem_22("xyz", 3))
print(problem_22("hello", -2))

print(problem_23("This is a sample sentence"))
print(problem_23("Short longestword"))
print(problem_23("One"))

print(problem_24([1, 2, 3, 4, 5], 2))
print(problem_24([1, 2, 3, 4, 5], -1))
print(problem_24([10, 20, 30], 3))

print(problem_25([1, 3, 5], [2, 4, 6]))
print(problem_25([1], [2]))
print(problem_25([], []))

print(problem_26("hello"))
print(problem_26("xyz"))
print(problem_26("AEIOU"))

print(problem_27([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
print(problem_27([[1]], [[2]]))
print(problem_27([[1, 2, 3], [4, 5, 6]], [[6, 5, 4], [3, 2, 1]]))

print(problem_28([[1, 2], [3, 4]]))
print(problem_28([[1]]))
print(problem_28([[1, 2, 3], [4, 5, 6]]))

print(problem_29("listen", "silent"))
print(problem_29("abc", "def"))
print(problem_29("aab", "aba"))

print(problem_30(10, 5))
print(problem_30(12, 18))
print(problem_30(7, 13))

print(problem_31("abc"),"problem_31")
print(problem_31("ab"),"problem_31")
print(problem_31("xyz"),"problem_31")

print(problem_32(5))
print(problem_32(1))
print(problem_32(10))

print(problem_33(123))
print(problem_33(0))
print(problem_33(999))

print(problem_34("This is a test sentence", ["a", "is"]))
print(problem_34("Hello world", ["hello", "world"]))
print(problem_34("One two three", ["two"]))

print(problem_35([3, 5, 1]))
print(problem_35([1]))
print(problem_35([2, 2, 2]))

print(problem_36("aaabbc"))
print(problem_36("abc"))
print(problem_36("aaaaa"))

print(problem_37("()"))
print(problem_37("([)]"))
print(problem_37("{[]}"))

print(problem_38(10))
print(problem_38(2))
print(problem_38(30))

print(problem_39("waterbottle", "erbottlewat"))
print(problem_39("abc", "cab"))
print(problem_39("hello", "llohe"))

print(problem_40([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(problem_40([[1]]))
print(problem_40([[1, 2], [3, 4], [5, 6]]))

print(problem_41([
    [5, 3, 0, 0],
    [6, 0, 0, 0],
    [0, 9, 8, 0],
    [0, 0, 0, 0]
]))
print(problem_41([[1, 2], [2, 1]]))
print(problem_41([[0, 0], [0, 0]]))

print(problem_42("name,age\nAlice,30\nBob,25"))
print(problem_42("x,y\n1,2"))
print(problem_42(""))

print(problem_43(["This", "is", "a", "test"], 10))
print(problem_43(["hello", "world"], 5))
print(problem_43(["one", "two", "three"], 15))

print(problem_44("A+B"))
print(problem_44("A+(B*C)"))
print(problem_44("(A+B)*C"))

print(problem_45([[0, 1], [0, 0]], (0, 0), (1, 1)))
print(problem_45([[0, 0, 1], [1, 0, 0], [0, 0, 0]], (0, 0), (2, 2)))
print(problem_45([[0]], (0, 0), (0, 0)))

print(problem_46("2024-12-11"))
print(problem_46("12/11/2024"))
print(problem_46("Dec 11, 2024"))

print(problem_47([[1, 3], [2, 6], [8, 10]]))
print(problem_47([[1, 4], [4, 5]]))
print(problem_47([]))

print(problem_48([1, 3, 2]))
print(problem_48([3, 2, 1]))
print(problem_48([1, 2, 3]))

print(problem_49("abc", "yabcx"))
print(problem_49("hello", "yellow"))
print(problem_49("test", "contest"))

print(problem_50("123"))
print(problem_50("-45"))
print(problem_50("0"))

print(problem_51("hello world", "l"))
print(problem_51("aaaa", "a"))
print(problem_51("test", "x"))

print(problem_52("hello hello hello", "hello"))
print(problem_52("ababab", "ab"))
print(problem_52("test", "x"))

print(problem_53("hello   world"))
print(problem_53("no    extra   spaces"))
print(problem_53("  multiple    "))

print(problem_54([1, 2, 3]))
print(problem_54([10, 10, 10]))
print(problem_54([5]))

print(problem_55("add", 10, 5))
print(problem_55("div", 10, 0))
print(problem_55("mul", -1, 5))

print(problem_56(6))
print(problem_56(28))
print(problem_56(12))

print(problem_57(3))
print(problem_57(1))
print(problem_57(5))

print(problem_58("Hello world"))
print(problem_58("one two three"))
print(problem_58("abc"))

print(problem_59(["apple", "banana", "apple", "cherry"]))
print(problem_59(["one", "one", "one"]))
print(problem_59([]))

print(problem_60([1, 2, 3, 2, 1]),"problem_60")
print(problem_60([1, 2, 2, 1]),"problem_60")
print(problem_60([1]),"problem_60")

print(problem_61(1),"problem_61")
print(problem_61(5),"problem_61")
print(problem_61(10),"problem_61")

print(problem_62([1, 2, 3]))
print(problem_62([4, 5, 6, 7]))
print(problem_62([10]))

print(problem_63([[1, 2, [3]], 4]))
print(problem_63([[1], [2, 3], [4, 5]]))
print(problem_63([]))

print(problem_64(5))
print(problem_64(0))
print(problem_64(1024))

print(problem_65("101"))
print(problem_65("0"))
print(problem_65("111111"))

print(problem_66("this is a test this is"))
print(problem_66("one two one"))
print(problem_66(""))

print(problem_67("this is a sentence"))
print(problem_67("hello world"))
print(problem_67("a"))

print(problem_68(5))
print(problem_68(1))
print(problem_68(10))

print(problem_69(2020))
print(problem_69(2024))
print(problem_69(2000))

print(problem_70("hello"))
print(problem_70("aabbcc"))
print(problem_70("abcabc"))

print(problem_71(1000, 0.05, 2))
print(problem_71(500, 0.1, 1))
print(problem_71(1000, 0, 3))

print(problem_72(0))
print(problem_72(100))
print(problem_72(-40))

print(problem_73([1, 2, 3, 4]))
print(problem_73([2, 2, 2]))
print(problem_73([1, 3, 5]))

print(problem_74([1, 2, 3, 4]))
print(problem_74([1, 1, 1]))
print(problem_74([]))

print(problem_75("hello, world!"))
print(problem_75("no punctuation"))
print(problem_75("test!!!"))

print(problem_76(12))
print(problem_76(100))
print(problem_76(17))

print(problem_77(112233))
print(problem_77(0))
print(problem_77(999999))

print(problem_78("abc"))
print(problem_78("aa"))
print(problem_78(""))

print(problem_79("a1b2c3"))
print(problem_79("abc"))
print(problem_79("123"))

print(problem_80("hello world", "o", "0"))
print(problem_80("aaaa", "a", "b"))
print(problem_80("test", "x", "y"))

print(problem_81([1, 2, 3, 4, 5], 3))
print(problem_81([10, 20, 30], 10))
print(problem_81([1], 1))

print(problem_82("Hello world"))
print(problem_82("one two"))
print(problem_82("abc"))

print(problem_83("hello", "ll"))
print(problem_83("abc", "d"))
print(problem_83("test", "t"))

print(problem_84(5))
print(problem_84(10))
print(problem_84(1))

print(problem_85([1, 2, 3], [3, 2, 1]))
print(problem_85([1, 2], [2, 2]))
print(problem_85([], []))

print(problem_86([{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}], "age", 30))
print(problem_86([{"x": 1}, {"x": 2}, {"y": 3}], "x", 2))
print(problem_86([], "x", 1))

print(problem_87([1, 2, 3]))
print(problem_87([3, 2, 1]))
print(problem_87([10, 9, 2, 5, 3, 7, 101, 18]))

print(problem_88(5))
print(problem_88(10))
print(problem_88(25))

print(problem_89([1, 2, 3, 4, 5]), "problem_89")
print(problem_89([2, 2, 2, 3, 3]), "problem_89")
print(problem_89([]), "problem_89")

print(problem_90(10, 5))
print(problem_90(10, 10))
print(problem_90(10, 15))

print(problem_91([1, 2, 3], [4, 5, 6]))
print(problem_91([0], [0]))
print(problem_91([1, 2], [2, 1]))

print(problem_92("abc", "a*c"))
print(problem_92("hello", "h?llo"))
print(problem_92("test", "t*st"))

print(problem_93([1, 2, 3]))
print(problem_93([10, 20, 30, 40]))
print(problem_93([]))

print(problem_94("test@example.com"))
print(problem_94("invalidemail"))
print(problem_94("name@domain"))

print(problem_95("babad"))
print(problem_95("cbbd"))
print(problem_95("a"))

print(problem_96("abc", 1))
print(problem_96("xyz", -1))
print(problem_96("hello", 3))

print(problem_97([("Alice", 30), ("Bob", 25), ("Charlie", 35)]))
print(problem_97([("X", 10), ("Y", 10)]))
print(problem_97([]))

print(problem_98(5))
print(problem_98(50))
print(problem_98(1))

print(problem_99("aabbcc"))
print(problem_99("abc"))
print(problem_99("aaaa"))

print(problem_100("123"))
print(problem_100("999"))
print(problem_100("111"))
