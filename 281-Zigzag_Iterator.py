"""
* Ref: https://discuss.leetcode.com/topic/24223/python-o-1-space-solutions
* Key points: No
* Explain your thought:
  - Change v1 and v2 into iterator, and store them in a matrix
  - When the "next" method is called, we alway return the top row of
    the matrix, and append this row to the bottom of the matrix to keep the
    zigzag property. How ever, if the length of this row is 1, don't append
    it.
  - When the method "hasNext" is called, just check if the matrix is empty.
    
* Compute complexity:
  - Time complexity: ?
  - Space complexity: O(n)
"""
class ZigzagIterator(object):
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.data = [(len(v), iter(v)) for v in (v1, v2) if v]

    def next(self):
        """
        :rtype: int
        """
        len, iter = self.data.pop(0)
        if len > 1:
            self.data.append((len-1, iter))
        return iter.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.data)
        
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())