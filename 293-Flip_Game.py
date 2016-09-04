"""
* Ref: https://discuss.leetcode.com/topic/49256/1-line-in-python
* Key points: No
* Explain your thought:
  - loop from the start of the string, check if there are consecutive '++',
    replace them into '--'
* Compute complexity:
  - Time complexity: O(n)
  - Space complexity: O(n)
"""
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return [s[:i] + "--" + s[i+2:] for i in range(len(s) - 1) if s[i] == s[i + 1] == "+"]
        