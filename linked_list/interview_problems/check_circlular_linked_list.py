from linked_list_node_class import Node


def circle_check(node):
    marker1 = node
    marker2 = node

    while marker2 is not None and marker2.next_node is not None:
        marker1 = marker1.next_node
        marker2 = marker2.next_node.next_node

        if marker2 == marker1:
            return True

    return False


a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c
c.next_node = a

print(circle_check(a))
