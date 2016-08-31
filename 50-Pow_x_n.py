"""
* Ref: No
* Key points:
* Explain your thought:
  - Use recusion
  - In recursion:
      1. if the power is even, double the base and divide the power by 2.
      2. if the power is odd, minus power by 1
* Compute complexity:
  - Time complexity: ?
  - Space complexity: O(n)
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Recursion:
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)
        
        # Iterative:
        # if n < 0:
        #     x = 1 / x
        #     n = -n
        # pow = 1
        # while n:
        #     if n & 1:
        #         pow *= x
        #     x *= x
        #     n >>= 1
        # return pow