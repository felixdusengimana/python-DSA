from linked_list_node_class import Node


def reverse(head):
    current = head
    previous = None
    next_node = None

    while current:
        next_node = current.next_node
        current.next_node = previous
        previous = current
        current = next_node

    return previous


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e

print(reverse(a).value)
