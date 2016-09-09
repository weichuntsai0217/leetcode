"""
* Ref: No
* Key points:
* Explain your thought:
  - loop numbers in each row
* Compute complexity:
  - Time complexity: O(m*n)
  - Space complexity: O(n)
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        for row in matrix:
            for col in row:
                if col == target: return True
                if target < col: break
        return False