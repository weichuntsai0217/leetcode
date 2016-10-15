# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res, level = [], [root]
        while level:
            res.append([ n.val for n in level ])
            level = [ kid for n in level for kid in (n.left, n.right) if kid]
        return res