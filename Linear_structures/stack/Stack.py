class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


s = Stack()
print(f"Is stack empty: {s.isEmpty()}")
s.push(1)
s.push(98)
s.push(3)
print(f"Size: {s.size()}")
s.pop()
print(f"Size: {s.size()}")
print(f"Peek: {s.peek()}")
print(s.isEmpty())
