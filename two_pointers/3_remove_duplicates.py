def remove_duplicates(nums):
    if len(nums) == 0:
        return 0
    
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write = write + 1
    
    return write


# Driver Code
def main():

    test_cases = [
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        [1, 1, 1, 1, 1],
    ]
    
    for i in range(len(test_cases)):
        print("Test Case #", i + 1)
        print("-" * 100)
        original = test_cases[i].copy()
        print("The input array is", original)
        length = remove_duplicates(test_cases[i])
        print("After removing duplicates, length is", length)
        print("Modified array (first", length, "elements):", test_cases[i][:length])
        print("-" * 100)


if __name__ == '__main__':
    main()
