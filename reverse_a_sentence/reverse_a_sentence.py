my_str="Welcome to Python"
my_str_spl=my_str.split()
my_str_len=len(my_str_spl) - 1

rev_str = []

while my_str_len >= 0:
    rev_str.append(my_str_spl[my_str_len])
    my_str_len -= 1
result = " ".join(rev_str)
print(result)