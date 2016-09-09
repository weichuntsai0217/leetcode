"""
* Ref: No
* Key points: 
* Explain your thought:
  - Sort the nums first
  - for each i, k pair, fint the max j (jmax) such that the threeSum
    is smaller than target. If we find this jmax, then for the cases
    in which i < j <= jmax are all counted.
* Compute complexity:
  - Time complexity: O(n^2)
  - Space complexity: O(n)
"""
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not len(nums): return 0
        if len(nums) == 1: return int( nums[0] < target )
        if len(nums) == 2: return int( sum(nums) < target )
        nums.sort()
        count, length = 0, len(nums)
        for k in xrange(2, length):
            i, j = 0, k-1
            while (i < j):
                if nums[i] + nums[j] + nums[k] < target:
                    count += j-i
                    i += 1
                else:
                    j -= 1
        return count