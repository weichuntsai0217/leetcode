"""
* Ref: https://discuss.leetcode.com/topic/55097/simple-python-solution
* Key points: The number of tabs is my depth and for each depth 
              I store the current path length.
* Explain your thought:
  - Given a default value 0 for the max absolute length of a file
  - Split the input string into lines by '\n'
  - Each line represents a file or a directory
  - Loop each line, if the current line represents a file,
    then get the length of the current absolute path and
    check if this length is larger than the max absolute length.
    If yes, replce it.
  - After loop, we could get the max absolute length of a file in this system.
* Compute complexity:
  - Time complexity: O(n)
  - Space complexity: O(n)
* Function inputs:
  - type input: str, ex: "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
* Function outputs:
  - rtype: int, ex: 20
"""

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxlen = 0 # the max file length I have to return
        pathlen = {0: 0} # The current path length (not including current directory or file) for each depth
        for line in input.splitlines(): # split the string into lines by '\n'
            name = line.lstrip('\t') # trim the left tabs of a line to get the current file or directory name
            depth = len(line) - len(name) # the number of tabs to define the depth
            if '.' in name: # the case for file
                maxlen = max(maxlen, pathlen[depth] + len(name)) # check if the current absolute path is the longest path
            else: # the case for directory
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1 # update the pathlen for the next depth
        return maxlen