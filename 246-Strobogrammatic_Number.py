"""
* Ref: No
* Key points:
* Explain your thought:
  - Use two indexes to retrieve the number pair from the head of the string and
    the end of the string.
* Compute complexity:
  - Time complexity: O(n/2)
  - Space complexity: O(n)
"""
class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        mapping = {'0':'0','1':'1','6':'9', '8':'8', '9':'6'}
        centers = '018'
        length = len(num)
        mid = length/2
        if length%2 and num[mid] not in centers: return False
        for i in xrange(mid):
            if (num[i] not in mapping) or (mapping[num[i]] != num[length-i-1]): return False
        return True