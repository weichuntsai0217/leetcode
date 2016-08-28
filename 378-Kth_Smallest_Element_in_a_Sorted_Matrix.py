"""
* Ref: No
* Key points: No
* Explain your thought:
  - use heapq.merge to merge arrays.
* Compute complexity:
  - Time complexity: ?
  - Space complexity: O(n)
"""

import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        return list(heapq.merge(*matrix))[k-1]