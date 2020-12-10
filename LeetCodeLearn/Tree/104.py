Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(log(n)), worst case O(n)
        """
        max_depth = 0
        stack = [[root, 1]]
        while stack:
            node, depth = stack.pop(-1)
            if node:
                if depth > max_depth:
                    max_depth = depth
                stack.append([node.right, depth + 1])
                stack.append([node.left, depth + 1])
        return max_depth