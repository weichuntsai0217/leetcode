class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        appeared = {}
        res = []
        for i in xrange(len(nums)):
            if nums[i] not in appeared:
                sub = nums[0:i] + nums[i+1:]
                res.append(reduce(lambda x,y: x*y, sub))
                appeared[nums[i]] = res[i]
            else:
                res.append(appeared[nums[i]])
        return res