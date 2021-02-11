"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten_iterative(self, head: 'Node') -> 'Node':
        if head:
            node = head
            stack = []
            while True:
                if node.child:
                    if node.next:
                        stack.append(node.next)
                    child = node.child
                    node.next = child
                    child.prev = node
                    node.child = None
                    node = child
                else:
                    if node.next is None:
                        if stack:
                            next_node = stack.pop()
                            next_node.prev = node
                            node.next = next_node
                            node = node.next
                        else:
                            break
                    else:
                        node = node.next

        return head

    def flatten_recursion(self, head: 'Node') -> 'Node':
        def _flatten(node):
            head = node
            while node:
                if node.child:
                    sub_h, sub_t = _flatten(node.child)
                    node.child = None
                    if node.next:
                        node_next = node.next
                        node.next = sub_h
                        sub_h.prev = node
                        node_next.prev = sub_t
                        sub_t.next = node_next
                    else:
                        node.next = sub_h
                        sub_h.prev = node
                        return head, sub_t
                if node.next:
                    node = node.next
                else:
                    break
            return head, node

        if head:
            head, tail = _flatten(head)
        return head

