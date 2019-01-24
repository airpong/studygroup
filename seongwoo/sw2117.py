for T in range(int(input())):
    n,m=list(map(int,input().split()))
    city=[]
    for i in range(n):
        city.append(list(map(int,input().split())))
    maxhome=0
    for i in range(n+1,0,-1):
        cost=i*i+(i-1)**2
        for j in range(n):
            for k in range(n):
                home=0
                for x in range(i):
                    for y in range(i-x):
                        if x==0 and y==0:
                            if city[j][k]:
                                home+=1
                        elif x==0 and y!=0:
                            if k+y<n:
                                if city[j][k+y]:
                                    home+=1
                            if k-y>=0:
                                if city[j][k-y]:
                                    home+=1
                        elif x!=0 and y==0:
                            if j+x<n:
                                if city[j+x][k]:
                                    home+=1
                            if j-x>=0:
                                if city[j-x][k]:
                                    home+=1
                        else:
                            if j+x<n and k+y<n:
                                if city[j+x][k+y]:
                                    home+=1
                            if j+x<n and k-y>=0:
                                if city[j+x][k-y]:
                                    home+=1
                            if j-x>=0 and k+y<n:
                                if city[j-x][k+y]:
                                    home+=1
                            if j-x>=0 and k-y>=0:
                                if city[j-x][k-y]:
                                    home+=1
                if cost<=home*m:
                    if maxhome<home:
                        maxhome=home
        if i>1 and (i-1)**2+(i-2)**2<maxhome:
            break
    print(f'#{T+1} {maxhome}')