# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if head is None or head.next is None:
            return head
        if head.next.next is None:
            return head
        head_odd = head
        tail_odd = head
        head_even = head.next
        tail_even = head.next
        while tail_odd.next and tail_even.next:
            if tail_odd.next and tail_odd.next.next:
                tail_odd.next = tail_odd.next.next
                tail_odd = tail_odd.next

            if tail_even.next and tail_even.next.next:
                tail_even.next = tail_even.next.next
                tail_even = tail_even.next

        tail_odd.next = head_even
        tail_even.next = None
        return head_odd

