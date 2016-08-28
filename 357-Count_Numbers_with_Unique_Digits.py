"""
* Ref: https://discuss.leetcode.com/topic/48442/python-recursion-solution
* Key points:
* Explain your thought:
  - Use the case for numbers with 3 digits as an example,
    1. calculate the case for 3-digit number with non-zero first digit
       -> 9*9*8 = 648
    2. calculate the case for 2-digit number with non-zero first digit
       -> 9*9 = 81
    3. calculate the case for 1-digit number with non-zero first digit
       -> 10
    4. the result is 648+81+10 = 739
  - To sum up, we can use recursion to solve this problem.
* Compute complexity:
  - Time complexity: O(n)
  - Space complexity: O(n)
"""
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 10:
           # digits larger than 10 with all unique is impossible,
           # we just calculate 10-digit case, so set n=10
           n = 10
        
        if n == 0: # simple case for numbers with 1 digit < 1
            return 1
        elif n == 1: # simple case for numbers with 1 digit < 10
            return 10
        else: 
        # numbers with 2 digits and above, we have to calculate the case
        # when the first digit is not zero and do recursion down to
        # the simple case.
            return 9 * reduce(lambda x, y : x * y, xrange(11-n, 10)) + self.countNumbersWithUniqueDigits(n - 1)