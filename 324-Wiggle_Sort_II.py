"""
* Ref: No
* Key points: No
* Explain your thought:
  - Example nums = [1,2,...,7]      Example nums = [1,2,...,8] 

    Small half:  4 . 3 . 2 . 1      Small half:  4 . 3 . 2 . 1 .
    Large half:  . 7 . 6 . 5 .      Large half:  . 8 . 7 . 6 . 5
    --------------------------      --------------------------
    Together:    4 7 3 6 2 5 1      Together:    4 8 3 7 2 6 1 5

* Compute complexity:
  - Time complexity: 
  - Space complexity: O(n)
"""
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        length = len(nums)
        half = length/2+1 if length%2 else length/2
        smaller = sorted(nums[:half], reverse=True)
        larger = sorted(nums[half:], reverse=True)
        nums[::2] = smaller
        nums[1::2] = larger