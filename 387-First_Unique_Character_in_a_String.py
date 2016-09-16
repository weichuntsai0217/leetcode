class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        for i, c in enumerate(s):
            if c not in freq:
                freq[c] = [i, 1]
            else:
                freq[c][1] += 1
        first = len(s)
        for c in freq:
            if freq[c][1] == 1 and freq[c][0] < first: first = freq[c][0]
        return first if first != len(s) else -1