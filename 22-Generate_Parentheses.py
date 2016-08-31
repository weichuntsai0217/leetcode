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
        s=''
        res=[]
        self.recur(res, n, n, s)
        return res
    
    def recur(self, res, left, right, s):
        if [left, right]==[0, 0]:
            res.append(s)
        if left>0:
            self.recur(res, left-1, right, s+'(')
        if left<right:
            self.recur(res, left, right-1, s+')')