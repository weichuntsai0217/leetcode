class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <=2: return len(nums)
        start, end  = 0, 1
        while (start < len(nums) and end < len(nums)):
            if nums[start] == nums[end]:
                if end - start > 1:
                    nums.pop(end)
                else:
                    end += 1
            else:
                start = end
                end += 1
        return len(nums)