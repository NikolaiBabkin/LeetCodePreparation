# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST_DFS(self, root: TreeNode, val: int) -> TreeNode:
        """
        DFS iterative
        Time Complexity: O(log(n))
        Space Complexity: O(D), where D is max depth, O(n) in worst case
        """
        stack = [root]
        while stack:
            node = stack.pop(-1)
            if node:
                if node.val == val:
                    return node
                else:
                    if node.val < val:
                        stack.append(node.right)
                    else:
                        stack.append(node.left)

        return None

