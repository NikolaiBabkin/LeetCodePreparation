# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth_recursive(self, root: Node) -> int:
        """
        Recursive approach
        Time Complexity: O(n)
        Space Complexity: O(log(n)), in worst case O(n)
        """
        if root is None:
            return 0
        if root.children is None:
            if root.val is None:
                return 0
            return 1

        cur_depth = 0
        for child in root.children:
            cur_depth = max(cur_depth, self.maxDepth(child))
        return cur_depth + 1

    def maxDepth_iterative(self, root: Node) -> int:
        """
        IterativeK approach
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if (root is None) or (root.val is None):
            return 0
        res = 1
        queue = [(root, 1)]
        while queue:
            node, depth = queue.pop(0)
            if node and (node.val is not None):
                res = max(res, depth)
                queue += [(itm, depth + 1) for itm in node.children]
        return res




