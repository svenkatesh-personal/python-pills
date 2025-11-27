class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def detect_cycle(head):
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return slow
    
    return None


def find_cycle_start(head):
    cycle_node = detect_cycle(head)
    
    if cycle_node is None:
        return None
    
    # Move one pointer to head, keep other at meeting point
    # Move both one step at a time until they meet
    ptr1 = head
    ptr2 = cycle_node
    
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
    return ptr1.data


def create_linked_list_with_cycle(values, cycle_pos):
    if not values:
        return None
    
    head = Node(values[0])
    current = head
    cycle_node = None
    
    if cycle_pos == 0:
        cycle_node = head
    
    for i in range(1, len(values)):
        current.next = Node(values[i])
        current = current.next
        if i == cycle_pos:
            cycle_node = current
    
    # Create cycle
    if cycle_node is not None:
        current.next = cycle_node
    
    return head


def print_linked_list_info(values, cycle_pos):
    if cycle_pos == -1:
        return " -> ".join(map(str, values)) + " (no cycle)"
    else:
        list_str = " -> ".join(map(str, values))
        return list_str + " -> (cycle back to index " + str(cycle_pos) + ", value " + str(values[cycle_pos]) + ")"


# Driver Code
def main():

    test_cases = [
        ([1, 2, 3, 4, 5], 2),      # Cycle starts at index 2 (value 3)
        ([1, 2, 3, 4, 5, 6], 0),   # Cycle starts at index 0 (value 1)
        ([1, 2, 3, 4, 5], -1),     # No cycle
        ([10, 20, 30, 40], 1),     # Cycle starts at index 1 (value 20)
        ([5, 10, 15], 2),          # Cycle starts at index 2 (value 15)
    ]
    
    for i in range(len(test_cases)):
        print("Test Case #", i + 1)
        print("-" * 100)
        values, cycle_pos = test_cases[i]
        print("The linked list is:", print_linked_list_info(values, cycle_pos))
        
        head = create_linked_list_with_cycle(values, cycle_pos)
        cycle_start = find_cycle_start(head)
        
        if cycle_start is None:
            print("No cycle detected")
        else:
            print("Cycle starts at node with value:", cycle_start)
        print("-" * 100)


if __name__ == '__main__':
    main()
