"""
* Ref: No
* Key points: No
* Explain your thought:
  - Get the length of linkedList
  - Get the index randomly in the range from 0 to length-1
  - Get the node corresponding to the index and return its value
* Compute complexity:
  - Time complexity: O(n)
  - Space complexity: O(n)
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import random
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.len = 0
        node = head
        while node:
            self.len += 1
            node = node.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        target = random.randrange(self.len)
        node = self.head
        for i in xrange(target):
            node = node.next
        return node.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()