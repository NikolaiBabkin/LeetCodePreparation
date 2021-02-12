# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        Approach: Make ring
        1. make ring & calculate length
        2. k = length % k
           k = length - k
        3. make from tail k steps and split linked list

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if head is None or head.next is None:
            return head
        if k == 0:
            return head
        length = 1
        node = head
        while node.next:
            node = node.next
            length += 1

        node.next = head
        k = k % length
        k = length - k
        for _ in range(k):
            node = node.next
        head = node.next
        node.next = None
        return head

