l=[]
for i in range(int(input())):
    l.append(list(map(int,input().split())))
    
d=dict()
for i in range(len(l)):
    for j in range(len(l)):
        if i == j:
            continue
        elif l[i][0] < l[j][0] and l[i][1] < l[j][1]: #덩치 작을때
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        # print(d,'a')
    if i not in d:
        # print(d, '1')
        d[i]=1
    else:
    
        d[i]+=1
        # print(d, 'c')
print(*d.values())