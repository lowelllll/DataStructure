class CircularQueue:

    def __init__(self, n):
        self.maxCount = n
        self.data = [None] * n
        self.count = 0
        self.front = -1
        self.rear = -1

    def size(self):
        return self.count

    def isEmpty(self):
        return self.size() == 0

    def isFull(self):
        return self.size() == self.maxCount

    def enqueue(self, x):
        if self.isFull():
            raise IndexError('Queue full')
        self.rear = (self.rear+1) % (self.maxCount)
        self.data[self.rear] = x
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Queue Empty')
        self.front = (self.front+1) % (self.maxCount)
        x = self.data[self.front]
        self.count -= 1
        return x

    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue Empty')
        return self.data[(self.front+1) % (self.maxCount)]


Q = CircularQueue(6)

Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)

Q.dequeue()

Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)

print('peek => ',Q.peek())
print('front =>',Q.front)

print('Q => ',end="")
for data in Q.data:
    print(data,end=" ")