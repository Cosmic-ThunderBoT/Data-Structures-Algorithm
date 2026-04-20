def check_similar(building_1, building_2):
  #TO DO
    l1=building_1
    l2=building_2
    def_output = "Similar"
    while l1 or l2:
        if (l1 == None and l2!=None) or (l1!=None and l2==None):
            def_output = "Not Similar"
            break
        elif l1.elem!=l2.elem:
            def_output = "Not Similar"
        l1=l1.next
        l2=l2.next
    return def_output