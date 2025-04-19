n=int(input())

a=0
b=1
if n==0:
    print(0)
elif n==1:
    print(1)
else:
    for i in range(n-1):
        new=a+b
        a=b
        b=new
    print(new)