"""
* Ref: No
* Key points:
* Explain your thought:
  - Remove right-top elements and down-left elements layr by layer.
* Compute complexity:
  - Time complexity: O(m+n) ?
  - Space complexity: O(n)
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        while (True):
            # Strip top and right elements
            if not matrix or not matrix[0]: return res
            res += matrix.pop(0)
            for row in matrix:
                res.append(row.pop())

            # Strip bottom and left elements
            if not matrix or not matrix[0]: return res
            res += matrix.pop()[::-1]
            for row in matrix[::-1]:
                res.append(row.pop(0))