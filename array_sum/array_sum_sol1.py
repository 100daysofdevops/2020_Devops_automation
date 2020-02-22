# Time Complexity: O(n)
# Space Complexity: O(1)


def arr_sum(arr,sum):
    i = 0
    j = len(arr) -1

    arr.sort()
    while(i < j):
        if arr[i] + arr[j] > sum:
            j-=1
        elif arr[i] + arr[j] < sum:
            i+=1
        else:
            print(arr[i],arr[j])
            i+=1
