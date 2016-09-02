"""
* Ref: No
* Key points: 
* Explain your thought:
  - Use DFS to traverse the tree
  - When we meet leaf case, we get a path.
* Compute complexity:
  - Time complexity: O(n)
  - Space complexity: O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root: return []
        res = []
        def _setPaths(node, prefix, res):
            path = (prefix+'->'+ str(node.val)) if prefix else str(node.val)
            if node.left:
                _setPaths(node.left, path, res)
            if node.right:
                _setPaths(node.right, path, res)
            if (not node.left) and (not node.right): 
                res.append(path)
        _setPaths(root, '', res)
        return res