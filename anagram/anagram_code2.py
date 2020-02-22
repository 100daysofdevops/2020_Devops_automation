def anagram_check(str1,str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False


    check = {}

    for letter1 in str1:
        if letter1 in check:
            check[letter1] += 1
        else:
            check[letter1] = 1


    for letter2 in str2:
        if letter2 in check:
            check[letter2] -= 1
        else:
            check[letter2] = 1

    for k in check:
        if check[k] != 0:
            return False


    return True


str1="dog"
str2="god"


anagram_check(str1,str2)