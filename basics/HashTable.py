def hashFunc(s, capacity):
    return sum(map(ord, s))%capacity



class HashTable:
    """ Hash table which uses strings for keys. Value can be any object.
        Example usage:
            ht = HashTable(10)
            ht.set('a', 1).set('b', 2).set('c', 3)
            ht.get('c') = 30
    """
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.size = 0
        self.keys = []
        self.groups = [ [] for i in xrange(capacity)  ]
        # Note, Never try:  self.groups = capacity*[[]]

        # Storage format:
        # self.groups = [ [ [key1, value], [key2, value] ], [ [key3, value] ] ]
        # The outmost list is the one which the hash function maps the index to. The next inner
        # Array is the list of objects in that storage cell. The 3rd level is the individual
        # item array, where the 1st item is the key, and the 2nd item is the value.
    
    def getCollision(self, group, key):
        for i, item in enumerate(group):
            if key == item[0]:
                return i
        return None
    
    def printAll(self, action):
        print '----' + action + '----'
        print self.capacity
        print self.size
        print self.keys
        print self.groups

    def addItem(self, group, key, obj):
        group.append([key, obj])
        self.size += 1
        self.keys.append(key)
        self.printAll('added')

    def updateItem(self, group, collidedIdx, obj):
        group[collidedIdx][1] = obj
        self.printAll('updated')

    def deleteItem(self, group, index, key):
        group.pop(index)
        self.size -= 1
        self.keys.remove(key)
        self.printAll('deleted')
    
    def set(self, key, obj):
        index = hashFunc(key, self.capacity)
        group = self.groups[index]
        if group:
            collidedIdx = self.getCollision(group, key)
            if collidedIdx != None:
                self.updateItem(group, collidedIdx, obj)
            else:
                self.addItem(group, key, obj)
        else:
            self.addItem(group, key, obj)
        return self

    def get(self, key):
        index = hashFunc(key, self.capacity)
        group = self.groups[index]
        for item in group:
            if key == item[0]:
                return item[1]
        return None

    def remove(self, key):
        index = hashFunc(key, self.capacity)
        group = self.groups[index]
        for i, item in enumerate(group):
            if key == item[0]:
                self.deleteItem(group, i, key)
                return self
        raise KeyError(key)


ht = HashTable(5)
ht.set('a', 1).set('b', 2).set('c', 3)
print '==========='
print ht.get('a')
print ht.get('b')
print ht.get('c')

ht.set('a', 5).set('b', 6).set('c', 7)
print '==========='
print ht.get('a')
print ht.get('b')
print ht.get('c')


ht.remove('a')
print '==========='
print ht.get('b')
print ht.get('c')

