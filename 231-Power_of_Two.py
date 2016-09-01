"""
* Ref: No
* Key points:
* Explain your thought:
  - Trivial
* Compute complexity:
  - Time complexity: O(log(n))
  - Space complexity: O(n)
"""
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n>=2:
            while (n%2 == 0):
                n/=2
        return n == 1