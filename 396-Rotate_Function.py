class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A: return 0
        res, delta = [sum([ i*num for i, num in enumerate(A)])], sum(A)
        
        for i in xrange(1, len(A)):
            tmp = res[i-1] + delta - len(A)*A[len(A)-i]
            res.append(tmp)

        return max(res)