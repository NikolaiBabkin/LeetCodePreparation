# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList_iterative(self, head: 'Node') -> 'Node':
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        def get_node_to_link(old):
            if old in visited:
                return visited[old]
            node = Node(old.val)
            visited[old] = node
            return node

        visited = dict()
        sentinel_new = Node(-1)
        sentinel_old = Node(-1, head)
        old_node = sentinel_old
        new_node = sentinel_new
        while old_node.next:
            new_node.next = get_node_to_link(old_node.next)

            old_node = old_node.next
            new_node = new_node.next

            if old_node.random is None:
                continue

            new_node.random = get_node_to_link(old_node.random)

        return sentinel_new.next

    def copyRandomList_recursion(self, head: 'Node') -> 'Node':
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        def recursion(old_node):
            if old_node is None:
                return None
            if old_node in visited:
                node = visited[old_node]
            else:
                node = Node(old_node.val)
                visited[old_node] = node
            node.next = recursion(old_node.next)
            node.random = recursion(old_node.random)

            return node

        visited = {}
        sentinel_old = Node(-1, head)
        sentinel_new = Node(-1)
        sentinel_new.next = recursion(sentinel_old.next)

        return sentinel_new.next

    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if head is None:
            return head
        node = head
        while node:
            new_node = Node(node.val, node.next)
            node.next = new_node
            node = new_node.next

        sentinel2 = Node(-1, head)
        sentinel1 = Node(-1, sentinel2)
        new = sentinel2
        while new.next:
            old = new.next
            new = old.next
            if old.random:
                new.random = old.random.next

        old = sentinel1
        new = sentinel2
        while True:
            old.next = new.next
            old = old.next
            if old is None:
                break
            new.next = old.next
            new = new.next

        return sentinel2.next
