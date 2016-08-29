"""
* Ref: https://discuss.leetcode.com/topic/44592/7-8-lines-o-1-java-python/2
* Key points:
* Explain your thought:
  - If a player wins, his moves must satisfy:
        some row is all filled with his moves or
        some col is all filled with his moves or
        the diagonal is all filled with his moves or
        the anti-diagonal is all filled with his moves
* Compute complexity:
  - Time complexity: O(nlogn) ?
  - Space complexity: O(n)
"""

class TicTacToe(object):
    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.count = collections.Counter()
        self.n = n
        

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        for i, x in enumerate((row, col, row+col, row-col)):
            # 4 cases to check:
            #   i=0 is for row check
            #   i=1 is for col check
            #   i=2 is for diagonal(labeled by row+col) check
            #   i=3 is for anti-diagonal(labeled by row-col) check
            self.count[i, x, player] += 1
            if self.count[i, x, player] == self.n:
                return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)