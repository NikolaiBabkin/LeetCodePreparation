# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, head_a: ListNode, head_b: ListNode):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if head_a is None or head_b is None:
            return None

        length_a = 1
        tail_a = head_a
        while tail_a.next:
            tail_a = tail_a.next
            length_a += 1

        length_b = 1
        tail_b = head_b
        while tail_b.next:
            tail_b = tail_b.next
            length_b += 1

        if tail_a != tail_b:
            return None

        node_a = head_a
        node_b = head_b
        if length_a >= length_b:
            for _ in range(length_a - length_b):
                node_a = node_a.next
        else:
            for _ in range(length_b - length_a):
                node_b = node_b.next
        while node_a:
            if node_a == node_b:
                return node_a
            node_a = node_a.next
            node_b = node_b.next
        return None


