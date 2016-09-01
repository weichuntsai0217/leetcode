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
        centers = '018'
        mapping = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
        }
        i, j = 0, len(num)-1
        while(i<=j):
            if num[i] not in mapping: return False
            if mapping[num[i]] != num[j]: return False
            if i == j and num[i] not in centers: return False
            i+=1
            j-=1
        return True