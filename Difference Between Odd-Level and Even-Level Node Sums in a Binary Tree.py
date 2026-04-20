def level_sum(root):

    if root is None:
        return 0

    node_lev = [(root, 0)]
    odd = 0
    even = 0
    x = 0

    while x < len(node_lev):
        node = node_lev[x][0]
        lev = node_lev[x][1]

        if lev % 2 == 0:
            even += node.elem
        else:
            odd += node.elem

        if node.left is not None:
            node_lev.append((node.left, lev + 1))

        if node.right is not None:
            node_lev.append((node.right, lev + 1))

        x += 1

    return odd - even