# Pattern-System Matrix

This matrix shows which Tier 1 systems each Tier 2 pattern primarily uses.

| Pattern | Primary System | Secondary System | Example Problem | Time Complexity |
|---------|---------------|------------------|-----------------|-----------------|
| **Two Pointers** | Arrays/Lists | - | 3Sum, Container With Most Water | O(n) |
| **Sliding Window** | Arrays/Strings | Hashing | Longest Substring Without Repeating | O(n) |
| **Fast & Slow Pointers** | Linked Lists | - | Detect Cycle, Find Middle | O(n) |
| **Merge Intervals** | Arrays | Sorting | Merge Intervals, Insert Interval | O(n log n) |
| **Cyclic Sort** | Arrays | - | Find All Missing Numbers | O(n) |
| **Topological Sort** | Graphs | - | Course Schedule, Alien Dictionary | O(V + E) |
| **Backtracking** | Recursion | Arrays/Strings | Permutations, N-Queens | O(2^n) to O(n!) |
| **Greedy** | Multiple | Sorting/Heaps | Meeting Rooms, Jump Game | Varies |
| **Advanced DP** | Dynamic Programming | Arrays/Graphs | Longest Common Subsequence | O(n²) to O(n³) |
| **Bit Manipulation** | Numbers/Arrays | - | Single Number, Power of Two | O(1) to O(n) |
| **Union-Find** | Graphs | Arrays | Number of Islands, Redundant Connection | O(α(n)) amortized |

## Pattern Details

### Two Pointers
- **Systems**: Arrays, Linked Lists
- **When to Use**: 
  - Need to process array from both ends
  - Finding pairs that meet criteria
  - In-place operations
- **Template**: Two indices moving toward each other or in same direction

### Sliding Window
- **Systems**: Arrays, Strings, Hashing
- **When to Use**:
  - Finding subarray/substring with specific property
  - Need to maintain window of elements
  - Optimization problems on contiguous subarrays
- **Template**: Expand window, then shrink while maintaining invariant

### Fast & Slow Pointers
- **Systems**: Linked Lists
- **When to Use**:
  - Cycle detection
  - Finding middle element
  - Finding kth element from end
- **Template**: Two pointers moving at different speeds

### Merge Intervals
- **Systems**: Arrays, Sorting
- **When to Use**:
  - Overlapping intervals
  - Scheduling problems
  - Range merging
- **Template**: Sort by start, merge overlapping

### Cyclic Sort
- **Systems**: Arrays
- **When to Use**:
  - Array contains numbers in range [1, n]
  - Need to find missing/duplicate numbers
  - In-place sorting of limited range
- **Template**: Place each number at its correct index

### Topological Sort
- **Systems**: Graphs (Directed Acyclic)
- **When to Use**:
  - Dependency resolution
  - Task scheduling
  - Build order problems
- **Template**: DFS or Kahn's algorithm

### Backtracking
- **Systems**: Recursion, Arrays, Strings
- **When to Use**:
  - Generate all combinations/permutations
  - Constraint satisfaction
  - Decision tree exploration
- **Template**: Choose, explore, unchoose

### Greedy
- **Systems**: Multiple (often Sorting, Heaps)
- **When to Use**:
  - Optimization problems
  - Local optimal leads to global optimal
  - Interval scheduling
- **Template**: Make locally optimal choice at each step

### Advanced DP Patterns
- **Systems**: Dynamic Programming, Arrays, Graphs
- **When to Use**:
  - Multiple state variables
  - 2D/3D DP
  - State compression
- **Template**: Extend basic DP with additional dimensions/states

### Bit Manipulation
- **Systems**: Numbers, Arrays
- **When to Use**:
  - Efficient operations on bits
  - Set operations
  - Optimization problems
- **Template**: Use bitwise operators (AND, OR, XOR, shift)

### Union-Find
- **Systems**: Graphs, Arrays
- **When to Use**:
  - Dynamic connectivity
  - Cycle detection in undirected graphs
  - Component merging
- **Template**: Union and Find operations with path compression

