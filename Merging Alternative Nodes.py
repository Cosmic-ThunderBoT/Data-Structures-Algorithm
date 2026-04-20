def merge_alternate(head1, head2):
    h_1 = head1
    h_2 = head2

    while h_1 is not None and h_2 is not None:
        temp1 = h_1.next
        temp2 = h_2.next

        h_1.next = h_2
        if temp1 is None:
            break

        h_2.next = temp1

        h_1 = temp1
        h_2 = temp2

    return head1