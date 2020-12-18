# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(nums)
        if n == 1:
            return TreeNode(nums[0])
        if n > 1:
            root = TreeNode(nums[n//2])
            if len(nums[:n//2]):
                root.left = self.sortedArrayToBST(nums[:n // 2])
            if len(nums[(n // 2 + 1):]):
                root.right = self.sortedArrayToBST(nums[(n // 2 + 1):])
            return root
        return None
