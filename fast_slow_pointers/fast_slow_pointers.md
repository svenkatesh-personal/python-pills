# Fast and Slow Pointers Problems

## Overview
The fast and slow pointers technique (also known as Floyd's Tortoise and Hare algorithm) uses two pointers that move through a data structure at different speeds. This pattern is particularly useful for solving problems involving linked lists and detecting cycles.

## Common Patterns
1. **Finding Middle**: Slow moves 1 step, fast moves 2 steps - when fast reaches end, slow is at middle
2. **Cycle Detection**: If there's a cycle, fast will eventually meet slow
3. **Finding Cycle Start**: After detecting cycle, can find where it begins
4. **Nth from End**: Use gap between pointers to find position from end

## Problems List

### 1. Middle of Linked List
- **File**: [1_middle_of_linked_list.py](file:///Users/svenkatesh/personal_projects/python-pills/fast_slow_pointers/1_middle_of_linked_list.py)
- **Pattern**: Fast and Slow Pointers (Floyd's Tortoise and Hare)
- **Description**: Find the middle node of a linked list using two pointers moving at different speeds
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### 2. Happy Number
- **File**: [2_happy_number.py](file:///Users/svenkatesh/personal_projects/python-pills/fast_slow_pointers/2_happy_number.py)
- **Pattern**: Fast and Slow Pointers (Cycle Detection)
- **Description**: Determine if a number is happy by detecting cycles in the sum of squared digits sequence
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)

### 3. Find Cycle Start in Linked List
- **File**: [3_cycle_start.py](file:///Users/svenkatesh/personal_projects/python-pills/fast_slow_pointers/3_cycle_start.py)
- **Pattern**: Fast and Slow Pointers (Floyd's Cycle Detection)
- **Description**: Detect if a cycle exists in a linked list and find the node where the cycle begins
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

#### Understanding Cycles in Linked Lists

**What is a Cycle?**

A cycle occurs when a node in the linked list points back to an earlier node instead of ending with NULL, creating an infinite loop.

**Normal Linked List (No Cycle):**
```
1 → 2 → 3 → 4 → 5 → NULL
```

**Linked List WITH a Cycle:**
```
1 → 2 → 3 → 4 → 5
        ↑         ↓
        ←←←←←←←←←←
```
Here, node 5 points back to node 3, creating a loop. The **cycle start** is node 3.

**Real-World Analogy:**

Think of it like a circular running track:
- You start at the entrance (node 1)
- You run straight for a bit (nodes 1 → 2)
- Then you enter the circular track (node 3 is where the circle starts)
- You keep running in circles (3 → 4 → 5 → back to 3)

**The Algorithm (Two Phases):**

1. **Phase 1 - Detect Cycle**: Use fast and slow pointers. If they meet, a cycle exists.
2. **Phase 2 - Find Start**: Move one pointer to head, keep other at meeting point. Move both one step at a time. Where they meet is the cycle start.

**Why is this useful?**
- Detecting infinite loops in data structures
- Finding bugs where circular references exist
- Memory leak detection
- Graph algorithms that need to detect cycles

---

## Additional Resources
- Fast and slow pointers is particularly useful for:
  - Finding middle of linked list
  - Detecting cycles in linked list
  - Finding the start of a cycle
  - Checking if a linked list is a palindrome
  - Finding the nth node from the end
  - Happy number problem
