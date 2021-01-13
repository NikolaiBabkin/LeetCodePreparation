from DS_Algorithms.tree.BST import BST

class Morris(BST):
    def __init__(self):
        super().__init__()

    def inorder(self):
        res = []
        current = self.root
        while current:
            if current.left:
                predecessor = current.left
                while predecessor.right and predecessor.right.val != current.val:
                    predecessor = predecessor.right
                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    res.append(current.val)
                    current = current.right
            else:
                res.append(current.val)
                current = current.right
        return res

    # TODO: write preorder traversal function
    # def preorder(self):
    #     pass

    # TODO: write postorder traversal function
    # def postorder(self):
    #     pass

