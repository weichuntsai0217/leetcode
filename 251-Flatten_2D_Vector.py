"""
* Ref: No
* Key points: 
* Explain your thought:
  - Use two indexes row and col to store the position for next
  - When hasNext is called, check if the row and col is resonable,
  - When next is called, just return the result by matrix[row][col] and update
    col by 1.
* Compute complexity:
  - Time complexity:  O(n) for __init__
  - Space complexity: O(n)
"""
class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = [row for row in vec2d if len(row)] # filter empty rows
        self.row = 0
        self.col = 0

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            val = self.vec2d[self.row][self.col]
            self.col += 1
            return val
        return None

    def hasNext(self):
        """
        :rtype: bool
        """
        if not len(self.vec2d): return False
        if self.col < len(self.vec2d[self.row]):
            return True
        elif self.row + 1 < len(self.vec2d):
            self.row += 1
            self.col = 0
            return True
        return False

        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())


# Another solution for no-filtering in init:
#     Ref: https://discuss.leetcode.com/topic/20896/my-python-solution
# class Vector2D:
#     def __init__(self, vec2d):
#         """
#         Initialize your data structure here.
#         :type vec2d: List[List[int]]
#         """
#         self.col = 0
#         self.row = 0
#         self.vec = vec2d

#     def next(self):
#         """
#         :rtype: int
#         """
#         result = self.vec[self.row][self.col]
#         self.col += 1
#         return result

#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         while self.row < len(self.vec): 
#         # The while statement is to skip empty row, ex:
#         # [
#         #     [1],
#         #     [],
#         #     [],
#         #     [2,5]
#         # ]
#             if self.col < len(self.vec[self.row]):
#                 return True
            
#             self.col = 0
#             self.row += 1
            
#         return False