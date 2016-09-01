"""
* Ref: https://discuss.leetcode.com/topic/20896/my-python-solution
* Key points: 
* Explain your thought:
  - Use two indexes row and col to store the position for next
  - When hasNext is called, check if the row and col is resonable,
    if not, move them to a resonable position as possible.
  - When next is called, just return the result by matrix[row][col] and update
    col by 1.
* Compute complexity:
  - Time complexity: each call for hasNext is O(n) for worst case
  - Space complexity: O(n)
"""
class Vector2D:
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.col = 0
        self.row = 0
        self.vec = vec2d

    def next(self):
        """
        :rtype: int
        """
        result = self.vec[self.row][self.col]
        self.col += 1
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.row < len(self.vec): 
        # The while statement is to skip empty row, ex:
        # [
        #     [1],
        #     [],
        #     [],
        #     [2,5]
        # ]
            if self.col < len(self.vec[self.row]):
                return True
            
            self.col = 0
            self.row += 1
            
        return False
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())