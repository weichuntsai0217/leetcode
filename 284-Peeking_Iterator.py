"""
* Ref: https://discuss.leetcode.com/topic/25308/simple-python-solution
* Key points: No
* Explain your thought:
  - Use an extra data "temp" to store the previous value of the iterator.
    
* Compute complexity:
  - Time complexity: O(1)
  - Space complexity: O(n)
"""
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.val = iterator.next() if iterator.hasNext() else None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.val

    def next(self):
        """
        :rtype: int
        """
        val = self.val
        self.val = self.it.next() if self.it.hasNext() else None
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.val)
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].