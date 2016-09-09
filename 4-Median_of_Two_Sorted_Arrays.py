import heapq
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a = list(heapq.merge(nums1, nums2))
        if len(a)%2:
            return a[len(a)/2]
        else:
            return (a[len(a)/2-1] + a[len(a)/2])/2.0