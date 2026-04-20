def smallest_level(root):
    if root is None:
        return {}

    level_count = [0]
    temp = [root]
    min_dic = {}
    x = 0

    while x < len(temp):
        node = temp[x]
        lvl = level_count[x]

        if lvl not in min_dic or node.elem < min_dic[lvl]:
            min_dic[lvl] = node.elem

        if node.left is not None:
            temp.append(node.left)
            level_count.append(lvl + 1)

        if node.right is not None:
            temp.append(node.right)
            level_count.append(lvl + 1)

        x += 1

    return min_dic