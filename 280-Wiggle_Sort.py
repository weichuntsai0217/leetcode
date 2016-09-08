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
        # Simple sol:
        # for i in range(len(nums)):
        #     nums[i:i+2] = sorted(nums[i:i+2], reverse=i%2)

        # Universal sol pattern for 280-Wiggle_Sort_I and 324-Wiggle_Sort_II:
        nums.sort()
        length = len(nums)
        half = length/2+1 if length%2 else length/2
        smaller = nums[:half]
        larger = nums[half:]
        nums[::2] = smaller
        nums[1::2] = larger