# Trivial solution:
"""
* Ref: No
* Key points:
* Explain your thought:
  - slice the array and find the maximum in the slicing part.
* Compute complexity:
  - Time complexity: all case O(nk-k^2)
  - Space complexity: O(n)
"""
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums: return []
        res = []
        for i in xrange(len(nums)-k+1):
            res.append( max(nums[i:i+k]) )
        return res


# Optimal solution:
"""
* Ref: No
* Key points:
* Explain your thought:
  - slice the array and find the maximum in the slicing part.
* Compute complexity:
  - Time complexity: worst case O(nk-k^2), best case O(n)
  - Space complexity: O(n)
"""
# class Solution(object):
#     def maxSlidingWindow(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         if not nums: return []
#         last, highest = nums[0], max(nums[:k])
#         res = [highest]
#         for i in xrange(1, len(nums)-k+1):
#             if highest == last:
#                 highest = max(nums[i:i+k])
#             elif nums[i+k-1] > highest:
#                 highest = nums[i+k-1]
#             res.append(highest)
#             last = nums[i]
#         return res