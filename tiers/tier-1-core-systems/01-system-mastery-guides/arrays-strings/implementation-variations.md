# Arrays & Strings: Implementation Variations

## In-Place Array Operations

### Reverse Array (O(1) space)
```python
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
```

### Rotate Array (O(1) space)
```python
def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    
    # Reverse entire array
    arr.reverse()
    # Reverse first k elements
    arr[:k] = arr[:k][::-1]
    # Reverse remaining elements
    arr[k:] = arr[k:][::-1]
```

### Remove Duplicates In-Place
```python
def remove_duplicates(arr):
    if not arr:
        return 0
    
    write_idx = 1
    for read_idx in range(1, len(arr)):
        if arr[read_idx] != arr[write_idx - 1]:
            arr[write_idx] = arr[read_idx]
            write_idx += 1
    
    return write_idx
```

## String Building Patterns

### StringBuilder Equivalent
```python
# For many concatenations
parts = []
for item in items:
    parts.append(str(item))
result = "".join(parts)  # O(n) total
```

### Character Frequency Counting
```python
# Method 1: Counter (most Pythonic)
from collections import Counter
freq = Counter(s)

# Method 2: Dictionary
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1

# Method 3: Array (if limited alphabet)
freq = [0] * 26  # For lowercase letters
for char in s:
    freq[ord(char) - ord('a')] += 1
```

## Common Array Patterns

### Prefix Sum
```python
def prefix_sum(arr):
    prefix = [0]
    for num in arr:
        prefix.append(prefix[-1] + num)
    return prefix

# Range sum query: O(1)
def range_sum(prefix, i, j):
    return prefix[j + 1] - prefix[i]
```

### Kadane's Algorithm (Maximum Subarray)
```python
def max_subarray(arr):
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
```

## Trade-offs

### Array vs List (Python)
- **Array**: Fixed size, more memory efficient, faster for numeric operations
- **List**: Dynamic size, more flexible, better for general use

### String Immutability
- **Immutability**: Prevents accidental modification, enables optimizations
- **Cost**: Concatenation creates new strings (use join for many operations)

