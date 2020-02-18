arr=[7,5,2,3,0,2,1]
my_dict={}for val in arr:
  if val in my_dict:
    print("Duplicate found", val)
  else:
    my_dict[val] = 1