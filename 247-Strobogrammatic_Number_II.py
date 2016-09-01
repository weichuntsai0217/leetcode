"""
* Ref: https://discuss.leetcode.com/topic/20750/3-lines-ruby-5-lines-python/2
* Key points:
* Explain your thought:
  - Choose the center of the string.
  - Append a pair of '00 11 88 69 96' to the left of the center and
    the right of the center until all combinations are done.
* Compute complexity:
  - Time complexity: 
  - Space complexity: O(n)
"""
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        nums = n%2 * list('018') or [''] # choose the center of the string
        while n > 1:
            n -= 2
            nums = [a + num + b for a, b in '00 11 88 69 96'.split()[n<2:] for num in nums]
        return nums