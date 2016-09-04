"""
* Ref: https://discuss.leetcode.com/topic/42522/python-94-5-simple-sum-array-on-one-dimension-o-n-for-both-update-and-sum
* Key points: No
* Explain your thought:
  - Create an accumulated matrix (AM) based on the original matrix (OM)
  - Each element in AM with row=i, col=j is the sum of elements from
    col=0 to col=j in row=i of OM.
  - Ex: 
        original matrix = 
        [
          [2,3,1],
          [9,8,7]
        ] 

        accumulated matrix =
        [
          [2,5,6],
          [9,17,24]
        ]
  - With AM, When call sumRegion, we dont always do O((row2-row1)*(col2-col1)) operations,
    We just sum the col2 from row1 to row2 and minus col1-1 from row1 to row2,
    that is O((row2-row1))
* Compute complexity:
  - Time complexity: 
  - Space complexity: O(n)
"""
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        for row in matrix:
            for col in xrange(1, len(row)):
                row[col] += row[col-1]
        self.matrix = matrix
        

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        original = self.matrix[row][col]
        if col != 0:
            original -= self.matrix[row][col-1]

        diff = val - original
        
        for y in xrange(col, len(self.matrix[0])):
            self.matrix[row][y] += diff

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum = 0
        for x in xrange(row1, row2+1):
            sum += self.matrix[x][col2]
            if col1 != 0:
                sum -= self.matrix[x][col1-1]
        return sum
        

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.update(1, 1, 10)
# numMatrix.sumRegion(1, 2, 3, 4)