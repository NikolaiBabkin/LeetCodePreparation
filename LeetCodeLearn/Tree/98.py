import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST_iterative(self, root: TreeNode) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if root is None:
            return True

        stack = [(root, -math.inf, math.inf)]
        while stack:
            node, low, high = stack.pop()
            if node.val <= low or node.val >= high:
                return False
            if node.right:
                stack.append((node.right, node.val, high))
            if node.left:
                stack.append((node.left, low, node.val))
        return True

    def isValidBST_recursion(self, root: TreeNode) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        def _is_valid(node, low=-math.inf, high=math.inf):
            if node is None:
                return True

            if node.val >= high or node.val <= low:
                return False

            left_res = _is_valid(node.left, low, node.val)
            right_res = _is_valid(node.right, node.val, high)
            return left_res and right_res

        return _is_valid(root)

