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
        self.d = {}
        for word in dictionary:
            abbr = word if len(word) <= 2 else word[0] + str(len(word) - 2) + word[-1]
            self.d[abbr] = word if abbr not in self.d else '' if self.d[abbr] != word else self.d[abbr]

    def isUnique(self, word):
        abbr = word if len(word) <= 2 else word[0] + str(len(word) - 2) + word[-1]
        return abbr not in self.d or self.d[abbr] == word


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")