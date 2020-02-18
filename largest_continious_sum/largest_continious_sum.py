def continious_sum(arr):
    # Checking edge cases to if the array length is zero
    if len(arr) == 0:
        return 0
    # Initializing the current and largest sum to the first element of the array
    current_sum=arr[0]
    largest_sum=arr[0]

    for num in arr[1:]:
        # Setting the current sum to the highest of two values
        current_sum = max(current_sum+num, num)
        # Setting the highest between the current and largest sum
        largest_sum = max(current_sum,largest_sum)
    return largest_sum

