# Arrays & Strings: When to Use

## Use Arrays When:

1. **Random Access Needed**
   - You need O(1) access to elements by index
   - Example: Binary search, accessing elements in any order

2. **Cache Locality Matters**
   - Sequential access patterns benefit from CPU cache
   - Example: Iterating through elements in order

3. **Fixed or Predictable Size**
   - Size is known or changes infrequently
   - Example: Fixed-size buffers, lookup tables

4. **Memory Efficiency**
   - Need contiguous memory layout
   - Example: Image processing, matrix operations

## Use Strings When:

1. **Text Processing**
   - Working with text data, parsing, formatting
   - Example: String matching, parsing logs

2. **Immutable Data**
   - Data shouldn't change after creation
   - Example: Configuration values, keys in dictionaries

3. **String-Specific Operations**
   - Need substring, pattern matching, regex
   - Example: Text search, validation

## Alternatives to Consider:

### Instead of Array, Consider:

- **Linked List**: If frequent insertions/deletions in middle
- **Hash Set/Map**: If need fast lookups by value (not index)
- **Heap**: If need to maintain sorted order with dynamic updates
- **BST**: If need sorted order with range queries

### Instead of String Concatenation, Consider:

- **StringBuilder (join)**: For many concatenations
- **List of strings**: Build list, join once at end
- **String formatting**: For template-based strings

## Decision Tree

```
Need to store data?
│
├─ Need random access by index?
│  ├─ Yes → Array
│  └─ No → Continue
│
├─ Need fast lookups by value?
│  ├─ Yes → Hash Set/Map
│  └─ No → Continue
│
├─ Need to maintain sorted order?
│  ├─ Yes → BST or Heap
│  └─ No → Continue
│
├─ Frequent insertions/deletions in middle?
│  ├─ Yes → Linked List
│  └─ No → Array
│
└─ Working with text?
   └─ Yes → String
```

## Common Mistakes

❌ **Using array for frequent lookups by value**
- Use hash set/map instead (O(1) vs O(n))

❌ **String concatenation in loops**
- Use join() instead (O(n) vs O(n²))

❌ **Using array when need sorted order**
- Use BST or heap for dynamic sorted data

❌ **Using array for frequent middle insertions**
- Use linked list (O(1) vs O(n))

