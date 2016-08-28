"""
* Ref: https://discuss.leetcode.com/topic/51356/two-python-solutions
* Key points:
  - To find out how much money I need to win the range lo..hi (the game starts 
    with the range 1..n), I try each possible x in the range (except hi, which 
    is pointless because hi-1 costs less and provides more information), 
    calculate how much I need when using that x, and take the minimum of
    those amounts.
  - Use bottom-up dynamic programming
* Explain your thought:

* Compute complexity:
  - Time complexity: O(n)
  - Space complexity: O(n)
"""

class Solution(object):
    def getMoneyAmount(self, n):
        need = [[0] * (n+1) for _ in range(n+1)]
        for lo in range(n, 0, -1):
            for hi in range(lo+1, n+1):
                need[lo][hi] = min(x + max(need[lo][x-1], need[x+1][hi])
                                   for x in range(lo, hi))
        return need[1][n]