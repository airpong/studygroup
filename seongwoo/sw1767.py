def search(ls,idx,link):
    global pro,linked,length,temp,linked
    nlink=link
    linklen=0
    if idx==len(ls):
        if linked<link:
            length=temp
            linked=link
        elif linked==link:
            if temp<length:
                length=temp
    else:
        c0,c1=ls[idx]
        # 상
        for i in range(c0-1,-1,-1):
            if pro[i][c1]:
                linklen=0
                break
            else:
                linklen+=1
        if linklen!=0:
            for i in range(c0-1,-1,-1):
                pro[i][c1]=2
            link+=1
            temp+=linklen
        if linklen!=0:
            search(ls,idx+1,link)
            temp-=linklen
            link=nlink
        if linklen!=0:
            for i in range(c0):
                pro[i][c1]=0
        linklen=0
        # 하
        for i in range(c0+1,n):
            if pro[i][c1]:
                linklen=0
                break
            else:
                linklen+=1
        if linklen!=0:
            for i in range(c0+1,n):
                pro[i][c1]=2
            link+=1
            temp+=linklen
        if linklen!=0:
            search(ls,idx+1,link)
            temp-=linklen
            link=nlink
        if linklen!=0:
            for i in range(c0+1,n):
                pro[i][c1]=0
        linklen=0
        # 좌
        for i in range(c1-1,-1,-1):
            if pro[c0][i]:
                linklen=0
                break
            else:
                linklen+=1
        if linklen!=0:
            for i in range(c1-1,-1,-1):
                pro[c0][i]=2
            link+=1
            temp+=linklen
        if linklen!=0:
            search(ls,idx+1,link)
            temp-=linklen
            link=nlink
        if linklen!=0:
            for i in range(c1):
                pro[c0][i]=0
        linklen=0
        # 우
        for i in range(c1+1,n):
            if pro[c0][i]:
                linklen=0
                break
            else:
                linklen+=1
        if linklen!=0:
            for i in range(c1+1,n):
                pro[c0][i]=2
            link+=1
            temp+=linklen
        if linklen!=0:
            search(ls,idx+1,link)
            temp-=linklen
            link=nlink
        if linklen!=0:
            for i in range(c1+1,n):
                pro[c0][i]=0
        linklen=0
        # 안함
        search(ls,idx+1,link)
for T in range(int(input())):
    n=int(input())
    pro=[]
    check_core=[]
    for i in range(n):
        pro.append(list(map(int,input().split())))
    for i in range(1,n-1):
        for j in range(1,n-1):
            if pro[i][j]:
                if pro[i-1][j] and pro[i+1][j] and pro[i][j-1] and pro[i][j+1]:
                    continue
                else:
                    check_core.append([i,j])
    link=0
    linked=0
    temp=0
    length=n*n
    search(check_core,0,0)
    print(f'#{T+1} {length}')