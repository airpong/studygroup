def choosing(ls):
    global m,c
    result=0
    for cre in range(2**m):
        target=bin(cre)[2:].zfill(m)
        choose=[]
        for search in range(m):
            if target[search]=='1':
                choose.append(ls[search])
        if sum(choose)<=c:
            answer=sum([x*x for x in choose])
            if result<answer:
                result=answer
    return result

for t in range(int(input())):
    n,m,c=list(map(int,input().split()))
    honeypots=[]
    maxnum=0
    for i in range(n):
        honeypots.append(list(map(int,input().split())))
    for j in range(n):
        for k in range(n-m+1):
            first=honeypots[j][k:k+m]
            maxnum1=choosing(first)
            maxnum2=0
            for sline in range(k+m,n-m+1):
                try:
                    second=honeypots[j][sline:sline+m]
                    maxnum2=choosing(second)
                except IndexError:
                    continue
            for nextj in range(j+1,n):
                for nextk in range(n-m+1):
                    second=honeypots[nextj][nextk:nextk+m]
                    temp=choosing(second)
                    if maxnum2<temp:
                        maxnum2=temp
            if maxnum<maxnum1+maxnum2:
                maxnum=maxnum1+maxnum2
    print(f'#{t+1} {maxnum}')