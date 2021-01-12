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

    def inorder(self):
        def _inorder(node: BST):
            if node:
                _inorder(node.left)
                res.append(node.val)
                _inorder(node.right)

        res = []
        _inorder(self.root)
        return res

    def preorder(self):
        def _preorder(node: BST):
            if node:
                res.append(node.val)
                _preorder(node.left)
                _preorder(node.right)

        res = []
        _preorder(self.root)
        return res

    def postorder(self):
        def _postorder(node: BST):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                res.append(node.val)

        res = []
        _postorder(self.root)
        return res

    def __str__(self):
        width = 4 * 2**self.max_depth - 3
        for i in range(self.max_depth + 1):
            pass



if __name__ == "__main__":
    tree = BST()
    values = [10,5,15,3,7,18, 6]
    for i in values:
        tree.insert(i)
        print(f'add {i} to Tree. Current max depth is {tree.max_depth}')

    tree.inorder()