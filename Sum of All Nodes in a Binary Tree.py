def sumTree(root):
    if root is None:
        return 0
    return root.elem + sumTree(root.left) + sumTree(root.right)