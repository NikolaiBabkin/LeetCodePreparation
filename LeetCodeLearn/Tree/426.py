class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        def inorder(node):
            if node.left is None and node.right is None:
                node.left = node
                node.right = node
                return node, node

            if node.left is None and node.right is not None:
                head_r, tail_r = inorder(node.right)
                node.right = head_r
                head_r.left = node
                return node, tail_r
            if node.left is not None and node.right is None:
                head_l, tail_l = inorder(node.left)
                tail_l.right = node
                node.left = tail_l
                return head_l, node
            if node.left is not None and node.right is not None:
                head_r, tail_r = inorder(node.right)
                head_l, tail_l = inorder(node.left)
                node.right = head_r
                head_r.left = node
                tail_l.right = node
                node.left = tail_l
            return head_l, tail_r

        if root is None:
            return root
        head_l, tail_r = inorder(root)
        head_l.left = tail_r
        tail_r.right = head_l
        return head_l

