"""
* Ref: No
* Key points:
* Explain your thought:
  - collect all node values into an array,
    sorting this array and get the element whose index is k-1
* Compute complexity:
  - Time complexity: O(n)
  - Space complexity: O(n)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root: return
        def setVals(node, vals):
            vals.append(node.val)
            if node.left:
                setVals(node.left, vals)
            if node.right:
                setVals(node.right, vals)
        vals = []
        setVals(root, vals)
        vals.sort()
        return vals[k-1]