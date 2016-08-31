"""
* Ref: No
* Key points:
* Explain your thought:
  - Use a stack to store and remove bracket pairs.
* Compute complexity:
  - Time complexity: O(n)
  - Space complexity: O(n)
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        stack = list()
        lefts = list('({[')
        pairs = {'(':')','{':'}','[':']'}
        for char in s:
            if char in lefts:
                stack.append(char)
            elif len(stack) and pairs[stack[-1]] == char:
                stack.pop()
            else:
                return False
        return not stack