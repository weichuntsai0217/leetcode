# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _traverseLeftLeaves(node, isLeft, lefts):
            if not node: return
            if isLeft and not node.left and not node.right:
                lefts.append(node.val)
            if node.left:
                _traverseLeftLeaves(node.left, True, lefts)
            if node.right:
                _traverseLeftLeaves(node.right, False, lefts)
                    
        lefts = []
        _traverseLeftLeaves(root, False, lefts)
        return sum(lefts)