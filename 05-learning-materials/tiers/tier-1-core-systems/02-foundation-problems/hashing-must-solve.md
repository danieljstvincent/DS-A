# Hashing: Must-Solve Foundation Problems

**Goal**: Master hash maps, hash sets, and frequency counting patterns.

## Essential Problems (10-15)

### Basic Hashing
- [ ] **Two Sum** (LeetCode 1)
  - System: Hashing
  - Pattern: Complement lookup
  - Complexity: O(n) time, O(n) space

- [ ] **Contains Duplicate** (LeetCode 217)
  - System: Hashing
  - Pattern: Set for uniqueness
  - Complexity: O(n) time, O(n) space

- [ ] **Valid Anagram** (LeetCode 242)
  - System: Hashing
  - Pattern: Frequency counting
  - Complexity: O(n) time, O(1) space (limited alphabet)

### Frequency Counting
- [ ] **Group Anagrams** (LeetCode 49)
  - System: Hashing
  - Pattern: Frequency map as key
  - Complexity: O(n * k) time, O(n * k) space

- [ ] **Top K Frequent Elements** (LeetCode 347)
  - System: Hashing + Heap
  - Pattern: Frequency map + heap
  - Complexity: O(n log k) time, O(n) space

- [ ] **First Unique Character** (LeetCode 387)
  - System: Hashing
  - Pattern: Frequency counting
  - Complexity: O(n) time, O(1) space

### Subarray/Substring Problems
- [ ] **Longest Substring Without Repeating Characters** (LeetCode 3)
  - System: Hashing + Sliding Window
  - Pattern: Character position tracking
  - Complexity: O(n) time, O(min(n, m)) space

- [ ] **Subarray Sum Equals K** (LeetCode 560)
  - System: Hashing
  - Pattern: Prefix sum + complement
  - Complexity: O(n) time, O(n) space

### Advanced
- [ ] **Longest Consecutive Sequence** (LeetCode 128)
  - System: Hashing
  - Pattern: Set for O(1) lookup
  - Complexity: O(n) time, O(n) space

- [ ] **Design HashMap** (LeetCode 706)
  - System: Hashing
  - Pattern: Implement from scratch
  - Complexity: O(1) average, O(n) worst case

- [ ] **Design HashSet** (LeetCode 705)
  - System: Hashing
  - Pattern: Implement from scratch
  - Complexity: O(1) average, O(n) worst case

## Key Concepts to Master

1. **Collision Handling**
   - Chaining vs Open Addressing
   - Load factor and rehashing

2. **When to Use Hash Map vs Hash Set**
   - Map: Need key-value pairs
   - Set: Need uniqueness check only

3. **Frequency Counting Patterns**
   - Counter for character/word frequencies
   - Prefix sum for subarray problems

## Mastery Checklist

- [ ] Can explain collision handling methods
- [ ] Can implement hash map from scratch
- [ ] Can identify when hashing is optimal
- [ ] Can use frequency counting effectively
- [ ] Understand load factor and rehashing

