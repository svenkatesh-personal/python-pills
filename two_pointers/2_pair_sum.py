def find_sum_of_two(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left = left + 1
        else:
            right = right - 1
    return False


# Driver Code
def main():

    test_cases = [
        ([1, 2, 3, 4, 6], 6),
        ([2, 5, 9, 11], 11),
        ([1, 3, 5, 7], 12),
        ([1, 2, 3, 4, 5], 10),
    ]
    
    for i in range(len(test_cases)):
        print("Test Case #", i + 1)
        print("-" * 100)
        print("The input array is", test_cases[i][0], "and the target sum is", test_cases[i][1])
        print("Does a pair exist that sums to the target?.....", find_sum_of_two(test_cases[i][0], test_cases[i][1]))
        print("-" * 100)


if __name__ == '__main__':
    main()
