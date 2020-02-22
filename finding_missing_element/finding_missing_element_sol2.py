def missing_element(arr1, arr2):
    arr1.sort()
    arr2.sort()

    mydict = {}

    for elem1 in arr1:
        if elem1 in mydict:
            mydict[elem1] += 1
        else:
            mydict[elem1] = 1

    for elem2 in arr2:
        if elem2 in mydict:
            mydict[elem2] -=1
        else:
            mydict[elem2] = 1


    for val in mydict:
        if mydict[val] != 0:
            return val

    return True