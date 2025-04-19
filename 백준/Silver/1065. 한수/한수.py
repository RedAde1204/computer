n=int(input())

def check(n):
    #등차수열 : 숫자가 규칙적으로 바뀌는 수열
    # 123 -> [1,2,3]
    n=str(n)
    l=[]
    for i in n:
        l.append(int(i))
    # print(l)
    if len(l)==1:
        return True
    nl=[]
    for i in range(len(l)-1): # 0,1,2
        nl.append(l[i]-l[i+1])
    if len(set(nl)) == 1:
        return True
    else:
        return False
#check(123469)

num=0
a=0
while 1:
    if a==n:
        break
    a+=1
    # if a가 등차수열을 이룰때
    if check(a) == True:
        num+=1
print(num)
