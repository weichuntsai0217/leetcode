"""
* Ref: https://discuss.leetcode.com/topic/49571/9-lines-recursive-without-helper
* Key points: 
* Explain your thought:
  - Use recursion, after plus one, if the node value is less than or equal to 9
    , just return this node to its parent, else set the node's value to 0 and
    make the node's parent plus 1.
* Compute complexity:
  - Time complexity: O(n)
  - Space complexity: O(n)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        if not head:
            return ListNode(1)  # handle the case when empty head
        plused = self.plusOne(head.next)
        head.val += plused != head.next
        if head.val <= 9:
            return head
        head.val = 0
        plused.next = head # handle the case when create new digit
        return plused