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
        res = []
        nums = [lower - 1] + nums + [upper+1]
        length = len(nums)
        for i in xrange(length):
            if (i+1 < length) and (nums[i] + 1 < nums[i+1]):
                start = nums[i] + 1
                end = nums[i+1] - 1
                res.append(str(start)+'->'+str(end) if start != end else str(start))
        return res
        
        