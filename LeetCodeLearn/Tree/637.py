# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        """
        Time Complexity: O(n)
        Space Complexity: O(D)
        """
        result = []
        level = 0
        dequeue = [(root, level)]
        level_sum = 0
        level_count = 0
        while dequeue:
            node, new_level = dequeue.pop(0)
            if new_level != level:
                result.append(level_sum / level_count)
                level_sum = 0
                level_count = 0
                level = new_level
            if node:
                dequeue.append((node.left, level + 1))
                dequeue.append((node.right, level + 1))
                level_sum += node.val
                level_count += 1
        return result
