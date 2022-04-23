class Queue2Stack:
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, element):
        self.instack.append(element)

    def dequeue(self):
        if not self.outstack:
            if not self.instack:
                return "No element in Queue."
            else:
                while self.instack:
                    self.outstack.append(self.instack.pop())

        return self.outstack.pop()


q = Queue2Stack()
for i in range(1, 11):
    q.enqueue(i)

for i in range(10):
    print(q.dequeue())
