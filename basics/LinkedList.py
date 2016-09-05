class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def getLength(self):
        return self.length

    def getNode(self, index):
        if index < 0 or index >  self.getLength()-1: return None
        node = self.head
        i = 0
        while node:
            if i == index: return node
            node = node.next
            i+=1

    def insert(self, index, val):
        if index < 0 or index > self.getLength(): return
        node = Node(val)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            prev = self.getNode(index-1)
            tmp = prev.next
            prev.next = node
            node.next = tmp
        self.length += 1

    def remove(self, index):
        if index < 0 or index > self.getLength()-1: return None
        node = None
        if index == 0:
            node = self.head
            self.head = self.head.next
        elif index == self.getLength()-1:
            prev = self.getNode(index-1)
            node = prev.next
            prev.next = None
        else:
            prev = self.getNode(index-1)
            prev.next = prev.next.next
        self.length -= 1
        return node


    def append(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            last = self.getNode(self.getLength()-1)
            last.next = node
        self.length += 1

if __name__ == '__main__':
    lt = LinkedList()
    lt.insert(0,'a')
    lt.append('c')
    lt.append('d')
    lt.insert(1, 'b')
    print lt.head.val
    print lt.head.next.val
    print lt.head.next.next.val
    print lt.head.next.next.next.val
    lt.remove(2)
    print lt.head.val
    print lt.head.next.val
    print lt.head.next.next.val
