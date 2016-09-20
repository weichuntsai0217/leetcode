import random
class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        idxs = [ i for i, num in enumerate(self.nums) if num == target ]
        return idxs[random.randrange(len(idxs))]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)