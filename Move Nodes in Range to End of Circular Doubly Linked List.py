def rangeMove(dhead1, start, end):
    temp = dhead1.next
    last = dhead1.prev
    point = last
    ex = []

    # traverse full circular list
    while temp != dhead1:
        new = temp.next

        if start <= temp.elem <= end:
            ex.append(temp.elem)

            # remove node
            temp.prev.next = temp.next
            temp.next.prev = temp.prev

        temp = new

    # append extracted values at end
    for i in ex:
        point.next = Node(i)
        point.next.prev = point
        point = point.next

    # reconnect circular links
    point.next = dhead1
    dhead1.prev = point

    return dhead1