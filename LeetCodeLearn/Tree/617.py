# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees_recursive(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        elif t2:
            t1 = t2

        return t1

    def mergeTrees_iterative(self, t1, t2):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if t1 and t2:
            queue1 = [t1]
            queue2 = [t2]
            while queue1 and queue2:
                node1 = queue1.pop(0)
                node2 = queue2.pop(0)
                node1.val += node2.val

                if node1.left and node2.left:
                    queue1.append(node1.left)
                    queue2.append(node2.left)
                elif node2.left:
                    node1.left = node2.left

                if node1.right and node2.right:
                    queue1.append(node1.right)
                    queue2.append(node2.right)
                elif node2.right:
                    node1.right = node2.right
            return t1
        elif t1:
            return t1
        elif t2:
            return t2
        return None


def create_tree(values):
    tree = [0] * len(values)
    tree[0] = TreeNode(values[0])
    for i in range(1, len(values)):
        if values[i]:
            tree[i] = TreeNode(values[i])
            if i % 2:
                tree[(i - 1)//2].left = tree[i]
            else:
                tree[(i - 2) // 2].right = tree[i]
    return tree[0]


def print_bfs(tree):
    queue = [tree]
    while queue:
        node = queue.pop(0)
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


if __name__ == "__main__":
    values_1 = [1,3,2,5]
    tree1 = create_tree(values_1)
    values_2 = [2,1,3,None,4,None,7]
    tree2 = create_tree(values_2)
    s = Solution()
    res = s.mergeTrees_iterative(tree1, tree2)
    print_bfs(res)


