"""
* Ref: No
* Key points:
* Explain your thought:
  - Traverse the BST with inorder, and collect the node's val into an array.
    Because of inorder traversal, the array is sorted automatically.
    When the lenth of the array equals to k, stop the recusion, and
    the last element in the array is our answer.
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
        def recur(node, res, k):
            if not node: return
            recur(node.left, res, k)
            if len(res) == k: return
            res.append(node.val)
            if len(res) == k: return
            recur(node.right, res, k)
            if len(res) == k: return
            
        res = []
        recur(root, res, k)
        return res[-1]

# Naive sol:
#  collect all node values into an array,
#  sorting this array and get the element whose index is k-1
# class Solution(object):
#     def kthSmallest(self, root, k):
#         """
#         :type root: TreeNode
#         :type k: int
#         :rtype: int
#         """
#         if not root: return
#         def setVals(node, vals):
#             vals.append(node.val)
#             if node.left:
#                 setVals(node.left, vals)
#             if node.right:
#                 setVals(node.right, vals)
#         vals = []
#         setVals(root, vals)
#         vals.sort()
#         return vals[k-1]