def sum_of_leaves(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.elem

    return sum_of_leaves(root.left) + sum_of_leaves(root.right)