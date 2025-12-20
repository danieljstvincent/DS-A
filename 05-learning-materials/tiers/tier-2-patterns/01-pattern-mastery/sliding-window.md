# Sliding Window Pattern

## Overview

The Sliding Window pattern maintains a window of elements that slides through the array/string, expanding and contracting based on conditions.

## When to Use

- Finding subarray/substring with specific property
- Need to maintain window of elements
- Optimization problems on contiguous subarrays
- Problems asking for "longest/shortest subarray with property X"

## Primary Systems

- **Arrays**: Most common
- **Strings**: Very common
- **Hashing**: Often combined for frequency tracking

## Pattern Template

### Template 1: Fixed Window Size
```python
def sliding_window_fixed(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### Template 2: Variable Window Size
```python
def sliding_window_variable(s):
    left = 0
    window = {}  # or set()
    max_len = 0
    
    for right in range(len(s)):
        # Expand window
        window[s[right]] = window.get(s[right], 0) + 1
        
        # Shrink window if needed
        while condition_to_shrink:
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
        
        # Update result
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

## Common Variations

1. **Fixed Size**: Window size is constant
   - Examples: Maximum sum of subarray of size k

2. **Variable Size**: Window expands/contracts
   - Examples: Longest substring without repeating characters

3. **With Hashing**: Track frequencies in window
   - Examples: Anagrams, character frequency problems

## Time & Space Complexity

- **Time**: Usually O(n) - each element visited at most twice
- **Space**: O(k) where k = window size, or O(min(n, m)) for character sets

## Key Insights

1. **Expand then shrink**: Usually expand window first, then shrink if needed
2. **Hash map for frequencies**: Track character/element counts efficiently
3. **Two pointers**: Left and right pointers define window boundaries

## Practice Problems

- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Longest Repeating Character Replacement
- Maximum Average Subarray
- Permutation in String

