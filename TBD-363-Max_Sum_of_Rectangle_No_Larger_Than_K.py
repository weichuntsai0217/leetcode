# ref: https://discuss.leetcode.com/topic/48930/any-accepted-python-solution/8

import bisect
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def maxSumSublist(vals):
            maxSum = float('-inf')
            prefixSum = 0
            prefixSums = [float('inf')]
            for val in vals:
                bisect.insort(prefixSums, prefixSum)
                prefixSum += val
                i = bisect.bisect_left(prefixSums, prefixSum - k)
                maxSum = max(maxSum, prefixSum - prefixSums[i])
            return maxSum
            
        maxSum = float('-inf')
        columns = zip(*matrix)
        print columns
        print len(columns)
        print len(matrix)
        for left in range(len(columns)):
            print 'letf: ', left
            rowSums = [0] * len(matrix)
            for column in columns[left:]:
                print 'column: ', column
                rowSums = map(int.__add__, rowSums, column)
                print 'rowSums: ', rowSums
                maxSum = max(maxSum, maxSumSublist(rowSums))
                print 'maxSum: ', maxSum
        return maxSum

if __name__ == '__main__':
    # matrix = [
    #   [1,  0, 1],
    #   [0, -2, 3]
    # ]
    matrix = [
      [1,  0, 1],
      [0, -2, 3]
    ]
    k = 2
    s = Solution()
    s.maxSumSubmatrix(matrix, k)


    ttt = map(int.__add__, [1,2,3] , [4,5,6])
    print 'ttt: ', ttt