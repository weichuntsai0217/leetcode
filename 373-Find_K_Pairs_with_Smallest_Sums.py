"""
* Ref: https://discuss.leetcode.com/topic/50450/slow-1-liner-to-fast-solutions/2
* Key points:
  - It turns each row into a generator of triples [u+v, u, v],
    only computing the next when asked for one. And then merges these
    generators with a heap. Takes O(m + k*log(m)) time and O(m) extra space.
* Explain your thought:
  - Get the generator of triples [u+v, u, v], and only computing the next
    when asked for one.
* Compute complexity:
  - Time complexity: O(m + k*log(m)) 
  - Space complexity: O(m)
"""
import heapq
import itertools
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        # Note!!!!! lambda u: ([u+v, u, v] for v in nums2) will return list containing generators. However,
        # lambda u: [[u+v, u, v] for v in nums2] will return list containing lists !!!  Tricky for [] and ()!!!
        streams = map(lambda u: ([u+v, u, v] for v in nums2), nums1)
        stream = heapq.merge(*streams)
        return [suv[1:] for suv in itertools.islice(stream, k)]
