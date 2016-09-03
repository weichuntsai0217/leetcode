"""
* Ref: No
* Key points: No
* Explain your thought:
  - Sorting the array pair by pair.
    If the index of the first element of the current pair is even,
    sorting the pair ascendant otherwise descendant
* Compute complexity:
  - Time complexity: ?
  - Space complexity: O(n)
"""
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            nums[i:i+2] = sorted(nums[i:i+2], reverse=i%2)