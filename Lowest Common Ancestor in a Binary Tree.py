def LCA(root, x, y):
    if root is None:
        return None

    if root.elem == x or root.elem == y:
        return root

    left_point = LCA(root.left, x, y)
    right_point = LCA(root.right, x, y)

    if left_point is not None and right_point is not None:
        return root

    if left_point is not None:
        return left_point

    return right_point