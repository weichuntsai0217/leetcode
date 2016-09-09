"""
* Ref: No
* Key points:
* Explain your thought:
  - Loop the number from the end of the array to the start of the array
* Compute complexity:
  - Time complexity: O(n)
  - Space complexity: O(n)
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits: return [1]
        i = len(digits)-1
        while i > -1:
            digits[i] += 1
            if digits[i] <= 9: return digits
            digits[i] = 0
            if i == 0: return [1] + digits
            i -= 1
        return digits