# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf_iterative(self, root: TreeNode) -> int:
        """
        Iterative DFS
        Time Complexity: O(n)
        Space Complexity: O(H)
        """
        res = 0
        stack = [(root, root.val)]
        while stack:
            node, number = stack.pop()
            if node.right:
                number_new = (number << 1) | node.right.val
                stack.append((node.right, number_new))
            if node.left:
                number_new = (number << 1) | node.left.val
                stack.append((node.left, number_new))
            if node.left is None and node.right is None:
                res += number
        return res

    def sumRootToLeaf_recursive(self, root: TreeNode) -> int:
        """
        Recursive DFS
        Time Complexity: O(n)
        Space Complexity: O(H)
        """
        def recursion_sum(node, number):
            nonlocal res
            if node.left is None and node.right is None:
                res += number
            else:
                if node.left:
                    number_new = (number << 1) | node.left.val
                    recursion_sum(node.left, number_new)
                if node.right:
                    number_new = (number << 1) | node.right.val
                    recursion_sum(node.right, number_new)

        res = 0
        recursion_sum(root, root.val)
        return res

    def sumRootToLeaf_morris(self, root: TreeNode) -> int:
        res = number = 0
        current = root
        while current:
            if current.left:
                predecessor = current.left
                steps = 1
                while predecessor.right and predecessor.right is not current:
                    predecessor = predecessor.right
                    steps += 1

                if predecessor.right is None:
                    number = (number << 1) | current.val
                    predecessor.right = current
                    current = current.left

                else:
                    if predecessor.left is None:
                        res += number

                    for _ in range(steps):
                        number >>= 1
                    predecessor.right = None
                    current = current.right


            else:
                number = (number << 1) | current.val
                if current.right is None:
                    res += number
                current = current.right

        return res
