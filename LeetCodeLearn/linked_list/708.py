# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if head is None:
            node = Node(insertVal)
            node.next = node
            return node

        # find min
        max_node = head
        while max_node.next != head:
            if max_node.val > max_node.next.val:
                break
            max_node = max_node.next
        if insertVal >= max_node.val or insertVal <= max_node.next.val:
            node = Node(insertVal, max_node.next)
            max_node.next = node
            return head
        curr = max_node.next
        while True:
            if curr.val <= insertVal <= curr.next.val:
                node = Node(insertVal, curr.next)
                curr.next = node
                break
            curr = curr.next
        return head
