def mirror_sum(root):

    def helper(left, right):
        if left is None and right is None:
            return 0

        if left is None or right is None:
            return 0

        total = left.elem + right.elem
        total += helper(left.left, right.right)
        total += helper(left.right, right.left)

        return total

    if root is None:
        return 0

    return helper(root.left, root.right)