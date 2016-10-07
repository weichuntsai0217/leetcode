class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        dp = ['1', '11']
        if n <= len(dp): return dp[n-1]
        i = len(dp)
        for i in xrange(len(dp), n):
            src, target, start = dp[i-1], '', 0
            for end in xrange(1, len(src)):
                if src[end] != src[start]:
                    target += (str(end-start) + src[start])
                    start = end
                    if end == len(src)-1: target += ('1' + src[end])
                elif end == len(src)-1:
                    target += (str(end-start+1) + src[start])
            dp.append(target)
        return dp[n-1]
                    