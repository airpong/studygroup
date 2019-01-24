def search(ls,x,y,dig):
    global n,k,road,longest,check
    high=ls[x][y]
    road.append([x,y])
    check[x][y]=1
    print(road)
    if x>0:
        if high>ls[x-1][y] and check[x-1][y]==0:
            search(ls,x-1,y,dig)
        elif dig==0 and check[x-1][y]==0:
            dig=1
            for k in range(1,k+1):
                if ls[x][y]>ls[x-1][y]-k:
                    temp,ls[x-1][y]=ls[x-1][y],ls[x-1][y]-k
                    search(ls,x-1,y,dig)
                    ls[x-1][y]=temp
            dig=0
    if x<n-1:
        if high>ls[x+1][y] and check[x+1][y]==0:
            search(ls,x+1,y,dig)
        elif dig==0 and check[x+1][y]==0:
            dig=1
            for k in range(1,k+1):
                if ls[x][y]>ls[x+1][y]-k:
                    temp,ls[x+1][y]=ls[x+1][y],ls[x+1][y]-k
                    search(ls,x+1,y,dig)
                    ls[x+1][y]=temp
            dig=0
    if y>0:
        if high>ls[x][y-1] and check[x][y-1]==0:
            search(ls,x,y-1,dig)
        elif dig==0 and check[x][y-1]==0:
            dig=1
            for k in range(1,k+1):
                if ls[x][y]>ls[x][y-1]-k:
                    temp,ls[x][y-1]=ls[x][y-1],ls[x][y-1]-k
                    search(ls,x,y-1,dig)
                    ls[x][y-1]=temp
            dig=0
    if y<n-1:
        if high>ls[x][y+1] and check[x][y+1]==0:
            search(ls,x,y+1,dig)
        elif dig==0 and check[x][y+1]==0:
            dig=1
            for k in range(1,k+1):
                if ls[x][y]>ls[x][y+1]-k:
                    temp,ls[x][y+1]=ls[x][y+1],ls[x][y+1]-k
                    search(ls,x,y+1,dig)
                    ls[x][y+1]=temp
            dig=0
    if longest<len(road):
        longest=len(road)
    del road[len(road)-1]
    print(longest)
    check[x][y]=0
for T in range(int(input())):
    n,k=list(map(int,input().split()))
    maps=[]
    maxhigh=0
    tips=[]
    road=[]
    for i in range(n):
        maps.append(list(map(int,input().split())))
        if maxhigh<max(maps[i]):
            maxhigh=max(maps[i])
    for i in range(n):
        for j in range(n):
            if maps[i][j]==maxhigh:
                tips.append([i,j])
    check=[[0 for i in range(n)] for j in range(n)]
    longest=0
    for peak in tips:
        search(maps,peak[0],peak[1],0)
    print(f'#{T+1} {longest}')