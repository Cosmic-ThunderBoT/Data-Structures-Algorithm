def find_path(root, key):
    path = []

    while root is not None:
        path.append(root.elem)

        if root.elem == key:
            return path

        if key < root.elem:
            root = root.left
        else:
            root = root.right

    return None