def pairJoin(dhead1, dhead2):
    temp1 = dhead1.next
    temp2 = dhead2.next
    point = dhead1

    while temp1 is not None and temp2 is not None:
        point.next = temp1
        temp1.prev = point
        point = temp1
        temp1 = temp1.next

        point.next = temp2
        temp2.prev = point
        point = temp2
        temp2 = temp2.next

    # attach remaining nodes of list1
    while temp1 is not None:
        point.next = temp1
        temp1.prev = point
        point = temp1
        temp1 = temp1.next

    # attach remaining nodes of list2
    while temp2 is not None:
        point.next = temp2
        temp2.prev = point
        point = temp2
        temp2 = temp2.next

    point.next = None  # end of DLL