def dfs(x,y,h,t,p) :
    global k,item,it
    #print(x,y,h,p,sep='//')
    if it < p :
        it = p
    real = item[y][x]
    if t == 0 :
        for i in range(0,k+1) :
            if x - 1 >= 0 and item[y][x-1] - i < h:
                # tmp = h
                # h = 100
                # visit.append((x,y))
                item[y][x] = 100
                dfs(x-1,y,item[y][x-1] - i,i,p+1)
                item[y][x] = real
                # h = tmp
            if x + 1 < n and item[y][x+1] -i < h:
                # tmp = h
                # h = 100
                # visit.append((x,y))
                item[y][x] = 100
                dfs(x+1,y,item[y][x+1] - i,i,p+1)
                # h = tmp
                item[y][x] = real
            if y - 1 >= 0 and item[y-1][x] - i < h:
                item[y][x] = 100
                # tmp = h
                # h = 100        
                # visit.append((x,y))    
                dfs(x,y-1,item[y-1][x] - i,i,p+1)
                item[y][x] = real
                # h = tmp
            if y + 1 < n and item[y+1][x] -i < h:
                item[y][x] = 100
                # tmp = h
                # h = 100
                # visit.append((x,y))
                dfs(x,y+1,item[y+1][x] - i,i,p+1)
                item[y][x] = real
                # h = tmp
    else :
        if x - 1 >= 0 and item[y][x-1] < h:
            # tmp = h
            # h = 100
            # visit.append((x,y))
            item[y][x] = 100
            dfs(x-1,y,item[y][x-1],t,p+1)
            item[y][x] = real
            # h = tmp
        if x + 1 < n and item[y][x+1] < h:
            # tmp = h
            # h = 100
            # visit.append((x,y))
            item[y][x] = 100
            dfs(x+1,y,item[y][x+1],t,p+1)
            # h = tmp
            item[y][x] = real
        if y - 1 >= 0 and item[y-1][x]< h:
            item[y][x] = 100
            # tmp = h
            # h = 100
            # visit.append((x,y))          
            dfs(x,y-1,item[y-1][x],t,p+1)
            item[y][x] = real
            # h = tmp
        if y + 1 < n and item[y+1][x] < h:
            item[y][x] = 100
            # tmp = h
            # h = 100
            # visit.append((x,y))
            dfs(x,y+1,item[y+1][x],t,p+1)
            item[y][x] = real
            # h = tmp
    return

for a in range(int(input())) :
    n,k = list(map(int,input().split()))
    item = [list(map(int,input().split())) for i in range(n)]
    high = 0
    my_max = 0
    
    for i in item :
        if max(i) > high :
            high = max(i)
    it = 0
    for i in range(n) :
        for j in range(n) :
            if item[j][i] == high :
                # print(i,j)
                # print(item)
                visit = []
                dfs(i,j,high,0,0)
                # print(i,j,high,it)
                # if it > my_max:
                #     my_max = it
    # it = 0
    # dfs(3,2,9,0,0)
    # print(it)

    print(f'#{a+1} {it+1}')