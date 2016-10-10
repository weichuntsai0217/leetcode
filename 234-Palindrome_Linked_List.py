# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s, node = [], head
        while node:
            s.append(node.val)
            node = node.next
        for i in xrange(len(s)/2):
            if s[i] != s[len(s)-1-i]: return False
        return True