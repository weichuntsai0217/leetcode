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
        for row in matrix:
            for num in row:
                if target < num: break
                if target == num: return True   
        return False