def search(boxi,boxj,x,y):
    global l
    li = [l[y][x]]
    top = 0
    x1 = x
    y1 = y
    for i in range(1,boxi):
        if x+i < n and y+i < n :
            k = l[y+i][x+i]
            if not k in li :
                li.append(k)
                # if x1 == 2 and y1 == 0 and boxi == 2 and boxj == 3:
                #     print(li)
            else :
                return -1
        else :
            return -1
    x+=i
    y+=i
    for j in range(1,boxj):
        if x-j >= 0 and y+j < n :
            k = l[y+j][x-j]
            if not k in li :
                li.append(k)
                # if x1 == 2 and y1 == 0 and boxi == 2 and boxj == 3:
                #     print(li)
            else :
                return -1
        else :
            return -1
    y += j
    x -= j
    for i in range(1,boxi):
        if x-i >= 0 and y-i >= 0 :
            k = l[y-i][x-i]
            if not k in li :
                li.append(k)
                # if x1 == 2 and y1 == 0 and boxi == 2 and boxj == 3:
                #     print(li)
            else :
                return -1
        else :
            return -1
    y-=i
    x-=i
    for j in range(1,boxj-1):
        if x+j < n and y-j >= 0 :
            k = l[y-j][x+j]
            if not k in li :
                li.append(k)
                # if x1 == 2 and y1 == 0 and boxi == 2 and boxj == 3:
                #    print(li)
            else :
                return -1
        else :
            return -1
    return len(li)


for a in range(int(input())) :
    n=int(input())
    l=[list(map(int,input().split())) for i in range(n)]
    my_max = -9999
    for x in range(1,n) :
        for y in range(n-1):
            for i in range(2,n) :
                for j in range(2,n) :
                    item = search(i,j,x,y)
                    if item > my_max :
                        my_max = item
    print(f'#{a+1} {my_max}')

