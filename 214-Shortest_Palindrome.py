"""
* Ref: https://discuss.leetcode.com/topic/14542/ac-in-288-ms-simple-brute-force
* Key points:
* Explain your thought:
  s          dedcba
  r[0:]      abcded    Nope...
  r[1:]   (a)bcded     Nope...
  r[2:]  (ab)cded      Nope...
  r[3:] (abc)ded       Yes! Return abc + dedcba
* Compute complexity:
  - Time complexity: O(n^2)
  - Space complexity: O(n)
"""
# ref: https://discuss.leetcode.com/topic/14542/ac-in-288-ms-simple-brute-force
class Solution:
    def shortestPalindrome(self, s):
        # @param {string} s
        # @return {string}
        r = s[::-1] # reverse the input string s
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s