# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST_inorder(self, root: TreeNode) -> TreeNode:
        nodes = []
        def inorder(node):
            if node:
                inorder(node.left)
                nodes.append(node.val)
                inorder(node.right)

        inorder(root)
        res = TreeNode(nodes.pop(0))
        next_node = res
        while nodes:
            next_node.right = TreeNode(nodes.pop(0))
            next_node = next_node.right
        return res


    def increasingBST_inorder_2(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                inorder(node.left)
                self.curr.right = TreeNode(node.val)
                self.curr = self.curr.right
                inorder(node.right)

        res = self.curr = TreeNode(None)
        inorder(root)
        return res.right


    def increasingBST_recursive(self, root: TreeNode) -> TreeNode:
        """
        Recursive approach
        Time Complexity: O(n)
        Space Complexity: O(log(n))

        Most difficult part is to avoid loops
        """
        def increasing(node):
            if node.left is None and node.right is None:
                head = node
                tail = node

            elif node.left and node.right:
                head_l, tail_l = increasing(node.left)
                head = head_l
                tail_l.right = TreeNode(node.val)
                tail = tail_l.right

                head_r, tail_r = increasing(node.right)
                tail.right = head_r
                tail = tail_r

            elif node.left:
                head_l, tail_l = increasing(node.left)
                head = head_l
                tail_l.right = TreeNode(node.val)
                tail = tail_l.right

            elif node.right:
                head_r, tail_r = increasing(node.right)
                head = TreeNode(node.val, None, head_r)
                tail = tail_r

            return head, tail


        fin_head, _ = increasing(root)
        return fin_head
