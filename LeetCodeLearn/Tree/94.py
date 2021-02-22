class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal_iterative(self, root: TreeNode) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        res = []
        node = root
        stack = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right

        return res

    def inorderTraversal_morris(self, root: TreeNode) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        res = []
        node = root
        while node:
            if node.left:
                curr = node.left
                while curr.right and curr.right != node:
                    curr = curr.right
                if curr.right is None:
                    curr.right = node
                    node = node.left
                else:
                    curr.right = None
                    res.append(node.val)
                    node = node.right
            else:
                res.append(node.val)
                node = node.right

        return res

    def inorderTraversal_recursion(self, root: TreeNode) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        def inorder(node):
            if node:
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)

        res = []
        inorder(root)
        return res
