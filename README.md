# Data Structures & Algorithms: Tier-Based Study System

This repository is organized using the **3-Tier System** from "Beyond the Coding Interview" to maximize interview preparation efficiency.

## 🎯 The 3-Tier Philosophy

### Tier 1: Core Computer Science Systems (Foundation)
**Master these FIRST** - They form 80-90% of coding interview questions.

- Arrays & Strings
- Hashing
- Linked Lists
- Stacks & Queues
- Trees
- Graphs
- Heaps
- Searching
- Sorting
- Recursion
- Basic Dynamic Programming

**Approach**: Depth over breadth. Master each system completely before moving on.

### Tier 2: Problem-Solving Patterns (Application)
**Only after Tier 1 mastery** - Recurring meta-patterns that combine Tier 1 systems.

- Two Pointers
- Sliding Window
- Fast & Slow Pointers
- Merge Intervals
- Cyclic Sort
- Topological Sort
- Backtracking
- Greedy
- Advanced DP Patterns
- Bit Manipulation
- Union-Find

**Approach**: Pattern recognition. Understand which patterns use which Tier 1 systems.

### Tier 3: Advanced & Hybrid Concepts (Differentiation)
**For senior/staff roles** - Complex problems combining multiple systems.

- Complex graph algorithms
- Advanced DP (state compression)
- Segment trees
- System design integration
- Concurrency problems

## 📁 Repository Structure

```
data-structures-and-algorithms/
│
├── tiers/
│   ├── tier-1-core-systems/          # START HERE
│   │   ├── 01-system-mastery-guides/ # Deep dive into each system
│   │   └── 02-foundation-problems/   # Must-solve problems per system
│   │
│   ├── tier-2-patterns/              # After Tier 1 mastery
│   │   ├── 01-pattern-mastery/      # Pattern guides and matrix
│   │   └── 02-pattern-problems/     # Problems by pattern
│   │
│   └── tier-3-advanced/             # For senior roles
│
├── solutions/
│   ├── tier-1/                      # Your Tier 1 solutions
│   ├── tier-2/                      # Your Tier 2 solutions
│   └── tier-3/                      # Your Tier 3 solutions
│
├── practice/
│   ├── tier-1-exit-exam.md          # Mastery checklist
│   ├── mastery-checklist.md         # Progress tracker
│   └── spaced-repetition/           # Review materials
│
└── resources/
    ├── blind-75-list.md             # Problem lists
    └── problem-lists/               # Additional resources
```

## 🚀 Getting Started

### Step 1: Start with Tier 1

1. **Review System Mastery Guides**
   - Read `tiers/tier-1-core-systems/01-system-mastery-guides/[system]/`
   - Study complexity cheatsheets
   - Understand implementation variations

2. **Solve Foundation Problems**
   - Work through `tiers/tier-1-core-systems/02-foundation-problems/[system]-must-solve.md`
   - Focus on 10-15 problems per system
   - Document your solutions in `solutions/tier-1/[system]/`

3. **Track Your Progress**
   - Update `practice/mastery-checklist.md`
   - Review complexity cheatsheets regularly

### Step 2: Take Tier 1 Exit Exam

Before moving to Tier 2, complete `practice/tier-1-exit-exam.md`.

**You're ready for Tier 2 when:**
- ✅ Score ≥90% on exit exam
- ✅ Can identify which system to use for any Tier 1 problem
- ✅ Can recite complexities from memory
- ✅ Can implement basic data structures in <10 minutes

### Step 3: Move to Tier 2 Patterns

1. **Study Pattern Guides**
   - Review `tiers/tier-2-patterns/01-pattern-mastery/`
   - Understand pattern-system matrix
   - Learn when to apply each pattern

2. **Practice Pattern Problems**
   - Solve problems in `tiers/tier-2-patterns/02-pattern-problems/`
   - Focus on pattern recognition
   - Document solutions in `solutions/tier-2/[pattern]/`

## 📚 Study Schedule

### Phase 1: Tier 1 Mastery (4-6 weeks)

- **Week 1-2**: Arrays, Strings, Hashing
- **Week 3**: Linked Lists, Stacks, Queues
- **Week 4**: Trees
- **Week 5**: Graphs
- **Week 6**: Heaps, Searching, Sorting, Recursion, Basic DP

### Phase 2: Tier 2 Patterns (3-4 weeks)

- **Week 1**: Two Pointers, Sliding Window, Fast & Slow Pointers
- **Week 2**: Merge Intervals, Cyclic Sort, Topological Sort
- **Week 3**: Backtracking, Greedy
- **Week 4**: Advanced DP, Bit Manipulation, Union-Find

### Phase 3: Tier 3 Advanced (2-3 weeks)

Only if interviewing for senior/staff roles or have mastered Tiers 1-2.

## 💡 Key Principles

1. **Tier 1 First**: Don't skip ahead. Master fundamentals before patterns.
2. **Depth Over Breadth**: Master 10 systems deeply > 500 problems superficially
3. **Understand Why**: Don't just memorize - understand trade-offs and when to use each system
4. **Practice Regularly**: Use spaced repetition to maintain mastery

## 🎓 Resources

- **Tier 1 Exit Exam**: `practice/tier-1-exit-exam.md`
- **Mastery Checklist**: `practice/mastery-checklist.md`
- **Pattern-System Matrix**: `tiers/tier-2-patterns/01-pattern-mastery/pattern-system-matrix.md`
- **Blind 75 List**: `resources/blind-75-list.txt`

## 📝 Notes

- Old directory structure has been archived in `archive/`
- Solutions are organized by tier and system/pattern
- Each system has mastery guides, complexity cheatsheets, and foundation problems

## ⚠️ Common Mistakes to Avoid

❌ **Jumping to Hard problems too early** - Master Tier 1 first
❌ **Memorizing without understanding** - Focus on why, not just how
❌ **Skipping complexity analysis** - Always know time/space complexity
❌ **Solving random problems** - Follow the tier system structure

---

**Remember**: The tier system is a filter. Start with Tier 1, prove mastery, then graduate. Candidates who follow this sequence have significantly higher success rates.
