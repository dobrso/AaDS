class EmptyStackError(Exception):
    pass

class QueueWithTwoStacks:
    def __init__(self):
        self.S1 = []
        self.S2 = []

    def enqueue(self, x):
        self.S1.append(x)

    def dequeue(self):
        if not(self.S2):
            if not(self.S1):
                raise EmptyStackError("Очередь пуста")

            while self.S1:
                self.S2.append(self.S1.pop())

        return self.S2.pop()

queue = QueueWithTwoStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue()) # 1
print(queue.dequeue()) # 2

queue.enqueue(4)

print(queue.dequeue()) # 3
print(queue.dequeue()) # 4

print(queue.dequeue()) # Exception