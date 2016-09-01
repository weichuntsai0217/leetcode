"""
* Ref: No
* Key points:
* Explain your thought:
  - Divide n by 3 until the remainder is not 0, and then
    check if the dividend is equivalent to 1
* Compute complexity:
  - Time complexity: O(log3(n))
  - Space complexity: O(n)
"""
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n>=3:
            while (n%3==0):
                n /= 3
        return n==1
        