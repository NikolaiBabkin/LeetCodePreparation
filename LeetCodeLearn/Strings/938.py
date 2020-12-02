# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert(root, key):
    if root is None:
        return TreeNode(key)
    if root.val == key:
        return root
    elif key > root.val:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


class Solution:
    # DFS
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        res = 0
        if root is None:
            return res

        if low <= root.val <= high:
            res += root.val
        if root.val > low:
            res += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            res += self.rangeSumBST(root.right, low, high)

        return res

    # # BFS
    # def rangeSumBST(self, root, L, R):
    #     ans = 0
    #     stack = [root]
    #     while stack:
    #         node = stack[0]
    #         if node:


if __name__ == "__main__":
    values = [10,5,15,3,7,18]
    tree = TreeNode(values[0])
    for i in values[1:]:
        tree = insert(tree, i)

    # inorder(tree)
    s = Solution()
    result = s.rangeSumBST(tree, 7, 15)

    print(f'rangeSumBST result: {result}')