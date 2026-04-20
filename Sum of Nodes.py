def sum_dist(head, arr):
  #TO DO
    sum =0
    for i in range (len(arr)):
        temp=head
        count=0
        while temp!=None:
            if count==arr[i]:
                sum += temp.elem
                break
            temp=temp.next
            count+=1
    return sum