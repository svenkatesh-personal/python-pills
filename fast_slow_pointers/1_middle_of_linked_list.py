class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_middle(head):
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    return slow.data


def create_linked_list(values):
    if not values:
        return None
    
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    
    return head


def print_linked_list(head):
    values = []
    current = head
    while current is not None:
        values.append(str(current.data))
        current = current.next
    return " -> ".join(values)


# Driver Code
def main():

    test_cases = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
        [1],
        [1, 2],
        [10, 20, 30, 40, 50, 60, 70],
    ]
    
    for i in range(len(test_cases)):
        print("Test Case #", i + 1)
        print("-" * 100)
        head = create_linked_list(test_cases[i])
        print("The linked list is:", print_linked_list(head))
        middle = find_middle(head)
        print("The middle element is:", middle)
        print("-" * 100)


if __name__ == '__main__':
    main()
