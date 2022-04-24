from linked_list_node_class import Node


def nth_to_last_node(n, head):
    left_pointer = head
    right_pointer = head

    for i in range(n-1):
        if not right_pointer.next_node:
            return "N is larger than the linked list."
        print(right_pointer.value, left_pointer.value)

        right_pointer = right_pointer.next_node

    while right_pointer.next_node:
        print(right_pointer.value, left_pointer.value)
        left_pointer = left_pointer.next_node
        right_pointer = right_pointer.next_node

    return left_pointer.value

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e
