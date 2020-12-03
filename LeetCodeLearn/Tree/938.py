from functions import memoty_usage
import random


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


class Solution(object):
    def _recursive_dfs_space_inefficient(self, root, low, high):
        res = 0
        if root is None:
            return res
        if low <= root.val <= high:
            res += root.val
        if root.val > low:
            res += self._recursive_dfs_space_inefficient(root.left, low, high)
        if root.val < high:
            res += self._recursive_dfs_space_inefficient(root.right, low, high)

        return res

    @memoty_usage
    def recursive_dfs_space_inefficient(self, root, low, high):
        """
        Recursive DFS over BST implementation.
        Time Complexity: O(n)
        Space Complexity: O(n), in each recursion call we reserve space for
        temporal variable 'res' in _recursive_dfs_space_inefficient function.
        :param root: Tree root
        :param low: low interval bounder
        :param high: high interval bounder
        :return: sum of all nodes values in [low, high]
        """
        return self._recursive_dfs_space_inefficient(root, low, high)

    def _recursive_dfs_space_efficient(self, root, low, high):
        if root:
            if low <= root.val <= high:
                self.res += root.val
            if root.val > low:
                self._recursive_dfs_space_efficient(root.left, low, high)
            if root.val < high:
                self._recursive_dfs_space_efficient(root.right, low, high)

    @memoty_usage
    def recursive_dfs_space_efficient(self, root, low, high):
        """
        Recursive DFS over BST implementation.
        Time Complexity: O(n)
        Space Complexity: O(1), temporal variable 'res' in _recursive_dfs_space_inefficient function
        isn't necessary, we can use class attribute 'self.res' as 'global' variable for the same reason as 'res'.
        :param root: Tree root
        :param low: low interval bounder
        :param high: high interval bounder
        :return: sum of all nodes values in [low, high]
        """
        self.res = 0
        self._recursive_dfs_space_efficient(root, low, high)
        return self.res

    @memoty_usage
    def iterative_dfs(self, root, low, high):
        """
        Deep First Search Iterative implementation. In Python we should chose iterative way
        instead recursive because of C stack limit. We couldn't call more than 1000 recursion in python.

        Time Complexity: O(n)
        Space Complexity: O(d), where d is max tree depth, in wars case O(d) ~ O(n)
        """
        res = 0
        stack = [root]
        while stack:
            node = stack.pop(-1)
            if node:
                if low <= node.val <= high:
                    res += node.val
                if node.val < high:
                    stack.append(node.right)
                if node.val > low:
                    stack.append(node.left)
        return res

    @memoty_usage
    def iterative_bfs(self, root, low, high):
        """
        Breadth Firs Search implementation.

        Time Complexity: O(n)
        Space Complexity: O(w), where w is max tree breadth, in worst case (full tree) O(w) ~ O(n)
        """
        res = 0
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                if low <= node.val <= high:
                    res += node.val
                if node.val > low:
                    queue.append(node.left)
                if node.val < high:
                    queue.append(node.right)
        return res


def run_test(values, low, high):
    tree = TreeNode(values[0])
    for i in values[1:]:
        tree = insert(tree, i)

    print(f'Nodes in Tree count: {len(values)}')
    s = Solution()
    print(f'Space Inefficient recursive DFS result: {s.recursive_dfs_space_inefficient(tree, low, high)}')
    print(f'Space Efficient recursive DFS result: {s.recursive_dfs_space_efficient(tree, low, high)}')
    print(f'Iterative DFS result: {s.iterative_dfs(tree, low, high)}')
    print(f'Iterative BFS result: {s.iterative_bfs(tree, low, high)}')


if __name__ == "__main__":
    print('Test case 1')
    values = [10,5,15,3,7,18]
    run_test(values, 7, 15)
    print('Test case 2')
    values = [10,5,15,3,7,13,18,1,6]
    run_test(values, 6, 10)
    print('Test case 3')
    values = []
    for i in range(1000):
        values.append(random.randint(1, 100000))
    values = list(set(values))
    run_test(values, 0, 100000)




