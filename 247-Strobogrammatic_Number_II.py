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
        if not n: return []
        pairs = [('0','0'),('1','1'),('6','9'),('8','8'),('9','6')]
        res = ['0', '1', '8'] if n%2 else ['']
        while len(res[0]) < n:
            if len(res[0]) == n-2: pairs.pop(0)
            res = [ l+c+r for c in res for (l, r) in pairs]
        return res