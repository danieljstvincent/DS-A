import timeit

setup = "s = 'abcdefghijklmnopqrstuvwxyz' * 1000"  # A string of length 26,000

# Original Solution
original = """
def problem_7(s: str):
    reversed_s = ""
    for i, letter in enumerate(s):
        reversed_s = letter + reversed_s 
    return reversed_s

result = problem_7(s)
"""

# Optimized Solution: Append and Reverse
optimized = """
def problem_7_efficient(s: str):
    reversed_chars = []
    for letter in s:
        reversed_chars.append(letter)
    reversed_chars.reverse()
    return ''.join(reversed_chars)

result = problem_7_efficient(s)
"""

# Optimized Solution: List Comprehension
comprehension = """
def problem_7_comprehension(s: str):
    reversed_chars = [s[i] for i in range(len(s)-1, -1, -1)]
    return ''.join(reversed_chars)

result = problem_7_comprehension(s)
"""

# Timing
original_time = timeit.timeit(original, setup=setup, number=10)
optimized_time = timeit.timeit(optimized, setup=setup, number=10)
comprehension_time = timeit.timeit(comprehension, setup=setup, number=10)

print(f"Original Solution Time: {original_time:.4f} seconds")
print(f"Optimized Solution Time: {optimized_time:.4f} seconds")
print(f"List Comprehension Solution Time: {comprehension_time:.4f} seconds")
