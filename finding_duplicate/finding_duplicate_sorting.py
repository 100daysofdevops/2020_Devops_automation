arr=[7,5,2,3,0,2,1]
arr.sort()for i in range(len(arr) -1):
  if arr[i] == arr[i+1]:
    print("Duplicate found", arr[i])