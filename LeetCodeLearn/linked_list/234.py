# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        def reverse_linked_list(head):
            if head is None or head.next is None:
                return head
            tail = head
            while tail.next:
                new_head = tail.next
                tail.next = tail.next.next
                new_head.next = head
                head = new_head
            return head

        def end_of_left(head):
            fast, slow = head, head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        if head is None or head.next is None:
            return True

        tail_l = end_of_left(head)
        head_r = tail_l.next
        head_r = reverse_linked_list(head_r)
        res = True
        node_l = head
        node_r = head_r
        while node_r:
            if node_l.val != node_r.val:
                res = False
            node_l = node_l.next
            node_r = node_r.next
        tail_l.next = reverse_linked_list(head_r)
        return res
