# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res, level, direction = [], [root], 1
        while level:
            res.append([ n.val for n in level ][::direction] )
            direction *= -1
            level = [ kid for n in level for kid in (n.left, n.right) if kid ]
        return res