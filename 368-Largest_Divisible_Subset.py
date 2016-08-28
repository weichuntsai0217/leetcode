"""
* Ref: 
* Key points: 
* Explain your thought:
  - Construct an ascending array, and each element in this array is divisible
    by the other elements which are smaller than it.
* Compute complexity:
  - Time complexity: 
  - Space complexity: 
"""

class Solution(object):
    def largestDivisibleSubset(self, nums):
        S = {-1: set()}
        for x in sorted(nums):
            S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
        return list(max(S.values(), key=len))
        