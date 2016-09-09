"""
* Ref: No
* Key points:
* Explain your thought:
  - Use recusion to put left bracket first, and then follow a right bracket or
    a left bracket.
* Compute complexity:
  - Time complexity: 
  - Space complexity: O(n)
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def recur(left, right, s, res):
            if not left and not right:
                res.append(s)
            if left:
                recur(left-1, right, s+'(', res)
            if left < right:
                recur(left, right-1, s+')', res)
        res = []
        recur(n, n, '', res)
        return res