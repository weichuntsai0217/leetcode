"""
* Ref: https://discuss.leetcode.com/topic/50779/o-n-k-python-solution
* Key points: 
* Explain your thought:
  - For each operation,
    just add the increment in the element at the startIndex
    and minus the increment in the element at the endIndex+1
* Compute complexity:
  - Time complexity: O(n+k)
  - Space complexity: O(n)
"""
class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * length
        for update in updates:
            start, end, inc = update
            res[start] += inc
            
            if end + 1 <= length - 1:
                res[end+1] -= inc

        sum = 0
        for i in range(length):
            sum += res[i]
            res[i] = sum
        return res