"""
* Ref: https://discuss.leetcode.com/topic/41870/real-iterator-in-python-java-c
* Key points:
  - An iterator shouldn't copy the entire data but just iterate over the
    original data structure.
  - I keep the current progress in a stack. My hasNext tries to find an 
    integer. My next returns it and moves on. I call hasNext in next because 
    hasNext is optional. Some user of the iterator might call only next and 
    never hasNext, e.g., if they know how many integers are in the structure 
    or if they want to handle the ending with exception handling.
* Explain your thought:
  - We build a stack with [nestedList, iterator_position] pairs,
    and always keep the flatten list-iterator_position pairs
    on the top of the stack.
* Compute complexity:
  - Time complexity: O(n)
  - Space complexity: O(n)
"""
# ref: https://discuss.leetcode.com/topic/41870/real-iterator-in-python-java-c
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [[nestedList, 0]]
        

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext(): return None

        # Get the flatten list on top of the stack and the iterator position.
        # The flatten list means [NestedInteger, NestedInteger]
        # and NestedInteger.isInteger is True
        nestedList, i = self.stack[-1] 

        self.stack[-1][1] += 1 # go to the next iterator postion
        return nestedList[i].getInteger()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        s = self.stack
        while s:
            nestedList, i = s[-1]
            if i == len(nestedList):
                s.pop()
            else:
                x = nestedList[i]
                if x.isInteger():
                    return True
                s[-1][1] += 1
                s.append([x.getList(), 0])
        return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())