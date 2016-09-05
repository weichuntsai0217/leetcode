class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty(): return self.items.pop(0)
        return None

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.isEmpty(): return self.items[0]
        return None

    def getSize(self):
        return len(self.items)


if __name__ == '__main__':
    q = Queue()
    q.push(-99)
    q.push('b')
    q.push(4)
    print q.getSize()
    print q.peek()
    print q.pop()
    print q.getSize()
    print q.peek()