"""
* Ref: https://discuss.leetcode.com/topic/24176/1-7-lines-python-length-prefixes
* Key points: 
* Explain your thought:
  - For each string s in the array, convert s into length of s followed by colon and s, and join them, ex: ['abc', 'dd'] => '3:abc2:dd'
  - Then decode is trivial, find the patter of number + colon and we can get
    the original strings.
* Compute complexity:
  - Time complexity: O(n) for encode, O(n) for decode
  - Space complexity: O(n)
"""
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return ''.join('%d:' % len(s) + s for s in strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        strs = []
        i = 0
        while i < len(s):
            j = s.find(':', i)
            i = j + 1 + int(s[i:j])
            strs.append(s[j+1:i])
        return strs
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))