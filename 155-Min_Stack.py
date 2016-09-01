"""
* Ref: No
* Key points:
* Explain your thought:
  - Store the minimum number for each level.
* Compute complexity:
  - Time complexity: O(1)
  - Space complexity: O(n)
"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.stack:
            currentMin = x if x < self.stack[-1][1] else self.stack[-1][1]
            self.stack.append((x,currentMin))
        else:
            self.stack.append((x,x))
        

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()