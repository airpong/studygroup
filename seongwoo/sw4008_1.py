def dfs(z,i):
    global maxnum
    global minnum
    if i==n:
        if maxnum < z:
            maxnum = z
        if minnum > z:
            minnum = z
    else:
        if o[0]>0:
            o[0]-=1
            dfs(z+numl[i],i+1)
            o[0]+=1
        if o[1]>0:
            o[1]-=1
            dfs(z-numl[i],i+1)
            o[1]+=1
        if o[2]>0:
            o[2]-=1
            dfs(z*numl[i],i+1)
            o[2]+=1
        if o[3]>0:
            o[3]-=1
            dfs(int(z/numl[i]),i+1)
            o[3]+=1

for i in range(int(input())):
    n=int(input())
    o=list(map(int,input().split()))
    numl=list(map(int,input().split()))
    maxnum = -100000001
    minnum = 100000001
    dfs(numl[0],1)
    print(f'#{i+1} {maxnum-minnum}')