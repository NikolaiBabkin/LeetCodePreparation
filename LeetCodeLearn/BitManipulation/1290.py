# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        res = head.val
        node = head.next
        while node:
            res = (res << 1) | node.val
            node = node.next

        return res