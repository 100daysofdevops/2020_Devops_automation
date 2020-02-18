s="AABBBCCCC"
count=0
fval=s[0]
s=s+" "
final_result=" "

for val in s:
    if val == fval:
        count +=1
    else:
        final_result = final_result + str(fval) + str(count)
        fval = val
        count =1
print(final_result)
