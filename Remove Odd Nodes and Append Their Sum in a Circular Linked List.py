def sumOddAppend(head):
    temp = head
    total = 0

    if head is None:
        return None

    # handle head separately if odd
    while head.elem % 2 != 0:
        total += head.elem

        # find last node
        last = head
        while last.next != head:
            last = last.next

        if head.next == head:  # only one node
            head = None
            break

        last.next = head.next
        head = head.next
        temp = head

    if head is None:
        if total > 0:
            new = Node(total)
            new.next = new
            return new
        return None

    curr = head.next

    while curr != head:
        if curr.elem % 2 != 0:
            total += curr.elem
            temp.next = curr.next
            curr = curr.next
        else:
            temp = curr
            curr = curr.next

    if total > 0:
        new = Node(total)
        temp.next = new
        new.next = head

    return head