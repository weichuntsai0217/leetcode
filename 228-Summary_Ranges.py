"""
* Ref: No
* Key points:
* Explain your thought:
  - Use two indexes to store the start index and the end index for a range.
    If start index = end index, return a single number range
    If end index > start index, return a '->' range.
* Compute complexity:
  - Time complexity: O(n)
  - Space complexity: O(n)
"""
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0: return []
        if len(nums) == 1: return [str(nums[0])]
        res, start = [], 0
        for i in xrange(len(nums)): # i is the end index of every range
            if (i+1 == len(nums)) or (nums[i+1] - nums[i] > 1):
                res.append( str(nums[start]) if start == i else str(nums[start]) + '->' + str(nums[i]) )
                start = i+1 # don't worry about i == len(nums), when it is this case, the loop is already the final run.
        return res