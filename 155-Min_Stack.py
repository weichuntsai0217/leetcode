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
        if not len(self.stack) or x < self.stack[-1][1] :
            self.stack.append([x, x])
        else: 
            self.stack.append([x, self.stack[-1][1]])

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()

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