"""
* Ref: https://discuss.leetcode.com/topic/23463/lucas-formula-maybe-o-1-and-3-4-liners
* Key points: 
* Explain your thought:
  - If we know f(4) with k colors, when we add the 5th pole, the 5th pole
    has 2 kind of choices to be paint:
    choice 1. the 5th pole's color is different from the 4th pole
    choice 2. the 5th pole's color is the same as the 4th pole 
              but different from the 3rd pole.
    So the answer will be the combination of choice 1 plus the combination of
    choice 2.
    For choice 1, it's aparently f(4)*(k-1).
    For choice 2, it's f(3)*(k-1), because in choice 2, the 4th and
    the 5th poles are the same color, and this combination equals that
    we pait the 4th pole with color different the 3rd pole.
  - If ways[i] is the number of ways to paint i posts, then:
    ways[0] = 0 (I think it should be 1, but whatever...)
    ways[1] = k
    ways[2] = k * k
    ways[i>2] = (ways[i-1] + ways[i-2]) * (k - 1)
    The i>2 case is like that because you can use the color for the last post just for the last post or for the two last posts, extending either the i-1 or the i-2 case, and in both cases, you must choose from the k-1 colors that the case you're extending didn't end with.

* Compute complexity:
  - Time complexity: 
  - Space complexity: O(n)
"""
# ref: https://discuss.leetcode.com/topic/23463/lucas-formula-maybe-o-1-and-3-4-liners
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        w = [0, k, k*k]
        while len(w) <= n:
            w.append( sum(w[-2:]) * (k-1) )
        return w[n]