"""
* Ref: No
* Key points:
* Explain your thought:
  - Find the n-th left most and n-th right-most vowels and exchange them
* Compute complexity:
  - Time complexity: O(n)
  - Space complexity: O(n)
"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        L = list(s)
        i, j = 0, len(L) - 1
        while i < j:
            while i < j and L[i].lower() not in vowels:
                i += 1
            while j > i and L[j].lower() not in vowels:
                j -= 1
            L[i], L[j] = L[j], L[i] 
            i += 1
            j -= 1
        return ''.join(L)