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
        lefts = {'(', '[', '{'}
        pairs = {')': '(', ']':'[', '}':'{'}
        stack = []
        for c in s:
            if c in lefts:
                stack.append(c)
            elif len(stack) and pairs[c] == stack[-1]:
                stack.pop()
            else:
                return False
        return not stack