from DS_Algorithms.tree.BST import BST
from DS_Algorithms.tree.morris_traversal import Morris

if __name__ == '__main__':
    bst = BST()
    morris_bst = Morris()

    tree = Morris()
    values = [10, 5, 15, 3, 7, 18, 6]
    for i in values:
        tree.insert(i)

    print(tree.inorder())