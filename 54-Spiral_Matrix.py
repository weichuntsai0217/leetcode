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
        rightTop = True
        while len(matrix) and len(matrix[0]):
            if rightTop:
                res += matrix.pop(0)
                for row in matrix:
                    res.append(row.pop())
                rightTop = False
            else:
                temp = matrix.pop()
                temp.reverse()
                res += temp
                for idx, row in enumerate(reversed(matrix)):
                    res.append(row.pop(0))
                rightTop = True
        return res