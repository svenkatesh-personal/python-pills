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

---

## Additional Resources
- Fast and slow pointers is particularly useful for:
  - Finding middle of linked list
  - Detecting cycles in linked list
  - Finding the start of a cycle
  - Checking if a linked list is a palindrome
  - Finding the nth node from the end
  - Happy number problem
