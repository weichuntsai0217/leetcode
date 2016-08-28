"""
* Ref: https://discuss.leetcode.com/topic/52320/4-liner-in-python-60ms/2
* Key points: No
* Explain your thought:
  - This is actually a typical stairs climbing problem.
    For example, if target is 4 and nums is an array of [1,2,3],
    then this problem is equivalent to calculate the number of ways for 
    climb­ing up a stair­case with total 4 steps by hopping either 1 step,
    2 steps, or 3 steps at a time.
  - The algorithm is trivival, if f(4) means the the number of ways for 
    climb­ing up a stair­case with 4 steps, then
    f(4) equals to f(4-1) + f(4-2) + f(4-3)
  - Here we use dynamic programming with bottom-up strategy. In the example
    above, we establish an array containing [f(0), f(1), f(2), f(3)],
    and we can get f(4)

* Compute complexity:
  - Time complexity: O(n)
  - Space complexity: O(n)
"""
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [1]
        for i in xrange(1, target+1):
            dp.append(sum(dp[i-n] for n in nums if i-n >= 0))
        return dp[target]

if __name__ == '__main__':
    nums = [2,5,1,7, 222]
    target = 15
    s = Solution()
    print s.combinationSum4(nums, target)