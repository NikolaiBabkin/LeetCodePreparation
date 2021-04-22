# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        def reverse(pre_head):
            tail = pre_head.next
            for _ in range(k - 1):
                new_head = tail.next
                tail.next = tail.next.next
                new_head.next = pre_head.next
                pre_head.next = new_head

            return tail

        if head is None or k == 1:
            return head

        sentinel = ListNode(-1, head)
        size = 0
        node = head
        while node:
            size += 1
            node = node.next

        cnt_to_reverse = size // k
        pre_head = sentinel
        for _ in range(cnt_to_reverse):
            pre_head = reverse(pre_head)

        return sentinel.next

