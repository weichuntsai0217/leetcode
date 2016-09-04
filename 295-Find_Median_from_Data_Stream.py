"""
* Ref: No
* Key points: No
* Explain your thought:
  - When we add a number, we have to sort it immediately.
  - We can use bisect.insort to do this
  - findMedian is trivial   
* Compute complexity:
  - Time complexity: O(1) for findMedian, O(n) for addNum
  - Space complexity: O(n)
"""
import bisect 
class MedianFinder:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        bisect.insort(self.data, num)

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.data) == 0: return 0
        if len(self.data) == 1: return self.data[0]
        q, r = len(self.data)/2, len(self.data)%2
        return self.data[q] if r else (self.data[q] + self.data[q-1])/2.0

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()