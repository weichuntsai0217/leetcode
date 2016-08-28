"""
* Ref: https://discuss.leetcode.com/topic/48473/python-one-liner
* Key points: 
* Explain your thought:
* Compute complexity:
  - Time complexity: O(n)
  - Space complexity: O(n)
"""
class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        return sorted( [ (a*num*num + b*num + c) for num in nums ] )
        