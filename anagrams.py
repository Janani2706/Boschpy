from collections import Counter 
s1 = "listen"
s2 = "little"

if len(s1) != len(s2):  
    print("No")
else:
    if Counter(s1) == Counter(s2):  
        print("Yes")
    else:
        print("No")