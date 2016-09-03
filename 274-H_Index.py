"""
* Ref: https://discuss.leetcode.com/topic/23810/python-o-n-lgn-time-with-sort-o-n-time-with-o-n-space
* Key points: 
* Explain your thought:
  - I think the better def is that, find all possible hs satisfy that 
    in my publications, there are at least h paper with citations >= h.
    And the biggest h is the answer.
* Compute complexity:
  - Time complexity: O(n)
  - Space complexity: O(n)
"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        n = len(citations)
        for i in xrange(n):
            if citations[i] >= (n-i):
                return n-i
        return 0
        