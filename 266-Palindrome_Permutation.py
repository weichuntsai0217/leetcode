"""
* Ref: No
* Key points: 
* Explain your thought:
  A string which can can permute palindrome must satisfy
  - if the length of this string is even, then all frequencies of 
    letters in this string must be even
  - if the length of this string is odd, then only one letter's 
    frequency is odd, others' frequencies must be even
* Compute complexity:
  - Time complexity: O(n)
  - Space complexity: O(n)
"""

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        r = len(s)%2
        src = list(s)
        freq = {}
        for char in src:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        vals = freq.values()
        if r:
            oddCount = 0
            for val in vals:
                if oddCount and val%2: return False
                elif val%2:
                   oddCount += 1
            return True
        else:
            for val in vals:
                if val%2: return False
            return True