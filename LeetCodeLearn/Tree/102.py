import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder_recursion(self, root: TreeNode) -> List[List[int]]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        def preorder(node, level):
            if node:
            if len(res) - 1 < level:
                res.append([node.val])
            else:
                res[level].append(node.val)
            preorder(node.left, level + 1)
            preorder(node.right, level + 1)

        res = []
        preorder(root, 0)
        return res


    def levelOrder_iterative(self, root: TreeNode) -> List[List[int]]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if root is None:
            return []
        res = []
        queue = collections.deque([root])
        while queue:
            sub_res = []
            for _ in range(len(queue)):
                node = queue.popleft()
                sub_res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if len(sub_res) > 0:
                res.append(sub_res)

        return res