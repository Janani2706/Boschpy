s = "Welcome to python"
words = s.split()
a = " "
for word in words:
    if(len(word)>len(a)):
        a = word
print("longest is:", a)