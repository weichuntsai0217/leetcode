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
        def recur(node, path, res):
            path = path + '->' + str(node.val) if path else str(node.val)
            if node.left: recur(node.left, path, res)
            if node.right: recur(node.right, path, res)
            if not node.left and not node.right:
                res.append(path)
        if not root: return []
        res = []
        recur(root, '', res)
        return res