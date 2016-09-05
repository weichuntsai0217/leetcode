class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty(): return self.items.pop()
        return None

    def peek(self):
        if not self.isEmpty(): return self.items[self.getSize()-1]
        return None

    def isEmpty(self):
        return len(self.items) == 0

    def getSize(self):
        return len(self.items)


if __name__ == '__main__':
    s = Stack()
    print(s.isEmpty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.getSize())
    print(s.isEmpty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.getSize())