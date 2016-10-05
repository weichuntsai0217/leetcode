class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        delta = len(haystack)-len(needle)+1
        for i in xrange(delta):
            if needle == haystack[i:len(needle)+i]: return i
        return -1
