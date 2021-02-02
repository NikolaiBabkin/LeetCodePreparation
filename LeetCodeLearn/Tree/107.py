# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = dict()
        deque = collections.deque([(root, 0)])
        while deque:
            node, level = deque.popleft()
            if level in res:
                res[level].append(node.val)
            else:
                res[level] = [node.val]
            if node.left:
                deque.append((node.left, level + 1))
            if node.right:
                deque.append((node.right, level + 1))

        return list(res.values())[::-1]

