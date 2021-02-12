# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        sentient = ListNode(0)
        node = sentient
        remember = 0
        while l1 and l2:
            val = l1.val + l2.val + remember
            remember = val // 10
            val = val % 10
            node.next = ListNode(val)
            node = node.next
            l1 = l1.next
            l2 = l2.next

        if l1 is None:
            l = l2
        else:
            l = l1
        while l:
            val = l.val + remember
            remember = val // 10
            val = val % 10
            node.next = ListNode(val)
            node = node.next
            l = l.next
        if remember > 0:
            node.next = ListNode(remember)

        return sentient.next
