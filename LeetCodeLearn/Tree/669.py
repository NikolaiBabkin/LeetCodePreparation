# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def is_lies_in_boundaries(node):
            return node.val >= low and node.val <= high

        def find_next_node(node):
            while node and not is_lies_in_boundaries(node):
                if node.val < low:
                    node = node.right
                else:
                    node = node.left
            return node

        root = find_next_node(root)
        if root:
            stack = [root]
            while stack:
                node = stack.pop(-1)
                if node.right:
                    node_right = find_next_node(node.right)
                    node.right = node_right
                    if node_right:
                        stack.append(node.right)
                if node.left:
                    node_left = find_next_node(node.left)
                    node.left = node_left
                    if node_left:
                        stack.append(node.left)

        return root

