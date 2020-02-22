def missing_element(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for elem1, elem2 in zip(arr1, arr2):
        if elem1 != elem2:
            return elem1

    return arr1[-1]