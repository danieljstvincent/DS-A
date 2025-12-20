# Two Pointers Pattern

## Overview

The Two Pointers pattern uses two pointers moving through a data structure (usually an array or linked list) to solve problems efficiently.

## When to Use

- Processing array/list from both ends
- Finding pairs that meet criteria
- In-place operations
- Problems that can be solved in O(n) time

## Primary Systems

- **Arrays**: Most common application
- **Linked Lists**: Also frequently used

## Pattern Template

### Template 1: Opposite Ends
```python
def two_pointers_opposite(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        # Process current pair
        if condition_to_move_left:
            left += 1
        elif condition_to_move_right:
            right -= 1
        else:
            # Found solution or process
            left += 1
            right -= 1
    
    return result
```

### Template 2: Same Direction
```python
def two_pointers_same(arr):
    slow = fast = 0
    
    while fast < len(arr):
        if condition_to_keep:
            arr[slow] = arr[fast]
            slow += 1
        fast += 1
    
    return slow  # or arr[:slow]
```

## Common Variations

1. **Opposite Ends**: Start from both ends, move toward center
   - Examples: Two Sum (sorted), Container With Most Water

2. **Same Direction**: Both pointers move forward
   - Examples: Remove duplicates, partition array

3. **Fast & Slow**: Different speeds (for linked lists)
   - Examples: Cycle detection, find middle

## Time & Space Complexity

- **Time**: Usually O(n) - single pass
- **Space**: Usually O(1) - no extra data structures

## Key Insights

1. **Sorted arrays**: Two pointers from ends is often optimal
2. **In-place operations**: Perfect for O(1) space solutions
3. **Pair finding**: Efficient alternative to nested loops

## Practice Problems

- Container With Most Water
- 3Sum
- Trapping Rain Water
- Valid Palindrome
- Remove Duplicates from Sorted Array

