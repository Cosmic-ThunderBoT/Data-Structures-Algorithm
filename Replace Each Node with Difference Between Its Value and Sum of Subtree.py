def subtract_summation(root):
    if root is None:
        return 0

    left_sum = subtract_summation(root.left)
    right_sum = subtract_summation(root.right)

    total = root.elem + left_sum + right_sum
    root.elem = root.elem - (left_sum + right_sum)

    return total