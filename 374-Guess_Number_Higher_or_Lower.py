"""
* Ref: https://discuss.leetcode.com/topic/51082/2-lines-as-usual
* Key points:
  - using binary search
* Explain your thought:
  - Just using binary search. Bisect the interval from 1 to n and use
    the guess API to check which interval is the answer in.
* Compute complexity:
  - Time complexity: O(log(N))
  - Space complexity: O(n)
"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) / 2
            if guess(mid) == 1:
                lo = mid + 1
            else:
                hi = mid
        return lo