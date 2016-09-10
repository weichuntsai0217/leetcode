"""
* Ref: No
* Key points: No
* Explain your thought:
  - Return true 
    if the input word's abbreviation is not in the abbreviation list 
    of the dictionary.
    or
    if the input word is in the dictionary and in this dictionary no other word has the same abbreviation as that of the input word.
    
* Compute complexity:
  - Time complexity: O(1) for isUnique, O(n) for __init__
  - Space complexity: O(n)
"""
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.d = {}
        for word in dictionary:
            abbr = word if len(word) <= 2 else word[0] + str(len(word)-2) + word[-1]
            s = '' if abbr in self.d and self.d[abbr] != word else word
            self.d[abbr] = s
            
                

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = word if len(word) <= 2 else word[0] + str(len(word)-2) + word[-1]
        return (abbr not in self.d) or (self.d[abbr] == word)


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")