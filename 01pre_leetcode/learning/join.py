""" .join() is a string method that combines element from an iterable(like a list) into a single string, with a separator between each element. """
import random

words = ['Hello', 'world', '!']
result = '-'.join(words)
print(result)

numbers = [12,43,213,43]
result_num = '-'.join(str(n) for n in numbers)
print(result_num)