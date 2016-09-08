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
        if n < 0:
            x, n = 1/x, -n
        res = 1
        while n:
            if n%2:
                res *= x
            x *= x
            n /= 2
        return res