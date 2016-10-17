# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        res = []
        def inorder(node, res):
            if node.left: inorder(node.left, res)
            res.append(node.val)
            if node.right: inorder(node.right, res)
        inorder(root, res)
        return all( res[i] < res[i+1] for i in xrange(len(res)-1))