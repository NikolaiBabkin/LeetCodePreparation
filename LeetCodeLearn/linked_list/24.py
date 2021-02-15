# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs_recursion(self, head: ListNode) -> ListNode:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        sentinel = ListNode(-1, head)
        if head and head.next:
            sentinel.next = head.next
            head.next = head.next.next
            sentinel.next.next = head
            head = sentinel.next
            head.next.next = self.swapPairs(head.next.next)
        return sentinel.next

    def swapPairs_iterative(self, head: ListNode) -> ListNode:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        sentinel = ListNode(-1, head)
        prev = sentinel
        curr = head
        while curr and curr.next:
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = curr
            prev = prev.next.next
            curr = prev.next

        return sentinel.next
