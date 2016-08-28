"""
* Ref: https://discuss.leetcode.com/topic/55930/1-liners-python-ruby
* Key points: use unicode sum for each string
* Explain your thought:
  - Get the unicode sum of each string, compute the difference of these sums.
  - Change the difference back to the letter.
* Compute complexity:
  - Time complexity: O(n)
  - Space complexity: O(n)
"""
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return chr(sum(map(ord, t)) - sum(map(ord, s)))