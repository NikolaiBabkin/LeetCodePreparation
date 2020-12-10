# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    @staticmethod
    def postorder_recursive(root: 'Node'):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        def _postorder(node):
            if node:
                for child in node.children:
                    _postorder(child)
                res.append(node.val)

        res = []
        _postorder(root)
        return res

    @staticmethod
    def postorder_iterative(root):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
            for c in root.children:
                stack.append(c)

        return output[::-1]
