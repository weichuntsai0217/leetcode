class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True
        def isAN(c):
            n = ord(c)
            return (n >= 48 and n<= 57 ) or (n >= 65 and n<= 90 ) or (n >= 97 and n<= 122 )
        res = [c.lower() for c in s if isAN(c) ]
        mid, length = len(res)/2, len(res)
        for i in xrange(mid):
            if res[i] != res[length-1-i]: return False
        return True