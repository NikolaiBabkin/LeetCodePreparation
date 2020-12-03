class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        self.root = None
        self.max_depth = 0

    def _insert(self, sub_root, val):
        depth = 0
        if sub_root is None:
            sub_root = Node(val)
        else:
            if val > sub_root.val:
                sub_root.right, sub_depth = self._insert(sub_root.right, val)
            if val < sub_root.val:
                sub_root.left, sub_depth = self._insert(sub_root.left, val)

            depth = 1 + sub_depth
        return sub_root, depth

    def insert(self, val):
        self.root, depth = self._insert(self.root, val)
        self.max_depth = max(self.max_depth, depth)

    def _search(self, sub_root, val):
        if sub_root is None:
            return None
        if sub_root.val == val:
            return sub_root
        elif val > sub_root.val:
            return self._search(sub_root.right, val)
        return self._search(sub_root.left, val)

    def search(self, val):
        return self._search(self.root, val)

    def _delete(self, sub_root, val):
        # if (sub_root.left is None) and (sub_root.right is None):
        pass

    def delete(self, val):
        return self._delete(self.root, val)

    def _inorder(self, sub_root):
        if sub_root:
            self._inorder(sub_root.left)
            print(sub_root.val)
            self._inorder(sub_root.right)

    def inorder(self):
        self._inorder(self.root)

    def __str__(self):
        width = 4 * 2**self.max_depth - 3
        for i in range(self.max_depth + 1):



if __name__ == "__main__":
    tree = BST()
    values = [10,5,15,3,7,18, 6]
    for i in values:
        tree.insert(i)
        print(f'add {i} to Tree. Current max depth is {tree.max_depth}')

    tree.inorder()