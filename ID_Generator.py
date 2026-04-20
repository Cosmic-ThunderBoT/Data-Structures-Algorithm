def idGenerator(head1, head2, head3):
    temp = head1
    string = ""
    while temp:
        string += str(temp.elem)
        temp = temp.next

    id = Node(string[-1])
    temp = id
    for i in range(len(string) - 2,-1,-1):
        temp.next = Node(string[i])
        temp = temp.next
    temp2 = head2
    temp3 = head3
    current = id
    while temp2 != None and temp3 != None:
        sum = 0
        sum += temp2.elem + temp3.elem
        temp2 = temp2.next
        temp3 = temp3.next
        if sum < 10:

            n_node = Node(sum)
            temp.next = n_node
            temp = temp.next
        else:
            sum2 = sum % 10
            n_node2 = Node(sum2)
            temp.next = n_node2
            temp = temp.next
    return id