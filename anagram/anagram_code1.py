def anagram(str1,str2):
  str1 = str1.replace(" ","").lower()
  str2 = str2.replace(" ","").lower()

  if sorted(str1) == sorted(str2):
    print("It's an anagram")
  else:
    print("Not an anagram")