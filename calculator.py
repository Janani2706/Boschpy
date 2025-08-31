def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
n1=int(input("enter no. "))
n2=int(input("enter no. "))
s = int(input("operation:"))
if s==1:
    print("sum is",add(n1,n2))
if s==2:
    print("sub is:",sub(n1,n2))
if s==3:
    print("mul is:",mul(n1,n2))
if s==4:
    print("div is:",div(n1,n2))