"""
* Ref: https://discuss.leetcode.com/topic/31922/6-line-python-with-two-guards
* Key points:
* Explain your thought:
  - Loop the array and use "two guards" method to compare
    the difference between the adjacent values.
* Compute complexity:
  - Time complexity: O(n)
  - Space complexity: O(n)
"""

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        prev, res = lower, []
        for i in [lower-1]+nums+[upper+1]:
            # lower-1 and upper+1 are to handle edge case
            if i - prev > 1:
                res += [str(prev+1)] if i-prev == 2 else [str(prev+1) + "->" + str(i-1)]
            prev = i
        return res
        
        