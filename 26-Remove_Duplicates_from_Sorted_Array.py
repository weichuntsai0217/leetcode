class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1: return len(nums)
        start, end = 0, 1
        while (start < len(nums) and end < len(nums)):
            if nums[end] == nums[start]:
                nums.pop(end)
            else:
                start = end
                end += 1
        return len(nums)