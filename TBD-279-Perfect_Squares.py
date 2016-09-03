# ref: https://discuss.leetcode.com/topic/23812/static-dp-c-12-ms-python-172-ms-ruby-384-ms/2
class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = self._dp
        while len(dp) <= n:
            dp.append( min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1 )
        return dp[n]
        
        