# Arrays & Strings: Complexity Cheatsheet

## Python List Operations

| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Access by index `arr[i]` | O(1) | O(1) | Direct memory access |
| Append `arr.append(x)` | O(1) amortized | O(1) | May trigger resize |
| Insert at index `arr.insert(i, x)` | O(n) | O(1) | Shifts all elements after i |
| Delete by index `del arr[i]` | O(n) | O(1) | Shifts all elements after i |
| Delete by value `arr.remove(x)` | O(n) | O(1) | Must search first |
| Search `x in arr` | O(n) | O(1) | Linear search |
| Slice `arr[i:j]` | O(k) where k=j-i | O(k) | Creates new list |
| Concatenate `arr1 + arr2` | O(n + m) | O(n + m) | Creates new list |
| Sort `arr.sort()` | O(n log n) | O(1) | In-place |
| Reverse `arr.reverse()` | O(n) | O(1) | In-place |

## String Operations

| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Access by index `s[i]` | O(1) | O(1) | Direct access |
| Concatenate `s1 + s2` | O(n + m) | O(n + m) | Creates new string (immutable) |
| Slice `s[i:j]` | O(k) where k=j-i | O(k) | Creates new string |
| Search substring `sub in s` | O(n * m) worst case | O(1) | Naive algorithm |
| `s.split()` | O(n) | O(n) | Creates list of substrings |
| `s.join(list)` | O(n) | O(n) | n = total length |
| `s.replace(old, new)` | O(n) | O(n) | Creates new string |

## StringBuilder Pattern (Python)

**Problem**: String concatenation in a loop is O(n²)

```python
# ❌ BAD: O(n²) time
result = ""
for char in chars:
    result += char  # Each += creates new string

# ✅ GOOD: O(n) time
result = "".join(chars)  # Single allocation
```

## Common Patterns

### Two Pointers
- **Time**: O(n)
- **Space**: O(1)
- **Use when**: Need to process array from both ends, or find pairs

### Sliding Window
- **Time**: O(n)
- **Space**: O(k) where k = window size
- **Use when**: Need to find subarray/substring with specific property

### Prefix Sum
- **Time**: O(n) preprocessing, O(1) queries
- **Space**: O(n)
- **Use when**: Need range sum queries

## When to Use Arrays vs Other Structures

| Use Case | Best Choice | Why |
|----------|-------------|-----|
| Random access by index | Array | O(1) access |
| Frequent insertions/deletions in middle | Linked List | O(1) insertion |
| Need to maintain sorted order | BST/Heap | Efficient ordering |
| Need fast lookups by value | Hash Set/Map | O(1) average lookup |
| Need to find min/max quickly | Heap | O(1) min/max |
| Sequential access only | Array | Better cache locality |

