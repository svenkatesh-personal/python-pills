def sum_of_squared_digits(number):
    total_sum = 0
    while number > 0:
        digit = number % 10
        total_sum = total_sum + (digit * digit)
        number = number // 10
    return total_sum


def is_happy_number(n):
    slow = n
    fast = n
    
    while True:
        slow = sum_of_squared_digits(slow)
        fast = sum_of_squared_digits(sum_of_squared_digits(fast))
        
        if fast == 1:
            return True
        if slow == fast:
            return False


# Driver Code
def main():

    test_cases = [19, 2, 7, 1, 23, 28, 100]
    
    for i in range(len(test_cases)):
        print("Test Case #", i + 1)
        print("-" * 100)
        print("Input number:", test_cases[i])
        result = is_happy_number(test_cases[i])
        print("Is it a happy number?.....", result)
        print("-" * 100)


if __name__ == '__main__':
    main()
