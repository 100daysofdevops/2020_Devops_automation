def seq_search(arr,ele):
    pos=0
    found=False

    while pos < len(arr) and not found:
        if arr[pos] == ele:
            found=True
        else:
            pos += 1

    return found