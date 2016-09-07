"""
* Ref: https://discuss.leetcode.com/topic/53344/simple-solution-in-python
* Key points: We just keep track of the index of the added elements,
              so when we remove them, we copy the last one into it.
              From Python docs (https://wiki.python.org/moin/TimeComplexity) 
              we know that list.append() takes O(1), both average and 
              amortized. Dictionary get and set functions take O(1) average,
              so we are OK.
* Explain your thought:
  - I just keep track of the index of the added elements by a dictionary,
    so when we remove them, we copy the last one into it.
    we know that list.append() takes O(1). 
    Dictionary get and set functions take O(1) average,
    so we are OK.
* Compute complexity:
  - Time complexity: average O(1) for insert, remove, and getRandom
  - Space complexity: O(n)
* Complexity requirement:
  - Design a data structure that supports all following 
    operations (insert, remove, and getRandom) in average O(1) time.
"""

import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.pos = [], {}
        
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos: return False
        self.nums.append(val)
        self.pos[val] = len(self.nums) -1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos: return False
        idx, last = self.pos[val], self.nums[-1]
        self.nums[idx], self.pos[last] = last, idx
        self.nums.pop()
        self.pos.pop(val)
        return True
            
    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randrange(len(self.nums))]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()