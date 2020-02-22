# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)


def arr_sum(arr,sum):
    for i in range(len(arr) -1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == sum:
                print(arr[i], arr[j])
    return False





