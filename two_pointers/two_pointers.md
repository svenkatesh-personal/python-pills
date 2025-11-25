# Two Pointers Problems

## Overview
The two pointers technique is a common algorithmic pattern used to solve array and string problems efficiently. It typically involves using two pointers that move through the data structure in a coordinated way.

## Common Patterns
1. **Opposite Direction**: Pointers start at both ends and move towards each other
2. **Same Direction**: Both pointers start at the beginning and move forward at different speeds
3. **Sliding Window**: Pointers define a window that expands or contracts based on conditions

## Problems List

### 1. Valid Palindrome
- **File**: [1_valid_palindrome.py](file:///Users/svenkatesh/personal_projects/python-pills/two_pointers/1_valid_palindrome.py)
- **Pattern**: Opposite Direction
- **Description**: Check if a string is a palindrome by comparing characters from both ends
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### 2. Pair Sum (Two Sum II)
- **File**: [2_pair_sum.py](file:///Users/svenkatesh/personal_projects/python-pills/two_pointers/2_pair_sum.py)
- **Pattern**: Opposite Direction
- **Description**: Find if there exists a pair of numbers in a sorted array that sum to a target value
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### 3. Remove Duplicates from Sorted Array
- **File**: [3_remove_duplicates.py](file:///Users/svenkatesh/personal_projects/python-pills/two_pointers/3_remove_duplicates.py)
- **Pattern**: Same Direction (Fast and Slow Pointers)
- **Description**: Remove duplicates from a sorted array in-place and return the new length
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

---

## Additional Resources
- Two pointers is particularly useful for:
  - Palindrome problems
  - Pair sum problems
  - Removing duplicates
  - Container with most water
  - Trapping rain water
  - Merging sorted arrays
