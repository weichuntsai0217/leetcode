"""
* Ref: No
* Key points: 
* Explain your thought:
  - Use an array called "nums" to record input values
  - Use an integer called "size" to constrain the length of "nums"
  - When the method "next" is called, check if the length of "nums" equals to
    "size", if yes -> pop the first element of nums
  - Append the new value into "nums"
  - return the average of elements in "nums"
* Compute complexity:
  - Time complexity: O(n)
  - Space complexity: O(n)
"""

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.nums = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.nums) == self.size: self.nums.pop(0)
        self.nums.append(val)
        return float(sum(self.nums))/len(self.nums)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)