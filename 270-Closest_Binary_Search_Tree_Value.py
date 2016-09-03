"""
* Ref: https://discuss.leetcode.com/topic/22590/4-7-lines-recursive-iterative-ruby-c-java-python
* Key points: 
* Explain your thought:
  - In the binary search tree, the value of the left child is less than
    the value of the parent node; the value of the right child is larger than
    the value of the parent node.
  - Use DFS and compare the node values of parent & child level by level.

* Compute complexity:
  - Time complexity: O(log(n))
  - Space complexity: O(n)
"""
# ref: https://discuss.leetcode.com/topic/22590/4-7-lines-recursive-iterative-ruby-c-java-python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        a = root.val
        kid = root.left if target < a else root.right
        if not kid: return a
        b = self.closestValue(kid, target)
        return min((b, a), key=lambda x: abs(target - x))
        