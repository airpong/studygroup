def move(item):
    global n
    
            # oklist.append((j[0],j[1]))
    return result
for a in range(int(input())) :
    n,m,k = list(map(int,input().split()))
    item = [list(map(int,input().split())) for i in range(k)]
    # 1 상 2 하 3 좌 4 우
    for time in range(m) :
        xylist = []
        result = []
        for i in item :
            if i[2] == 0 :
                continue
            if i[3] == 1:
                i[0] -= 1
                if i[0] == 0:
                    #i[0] = 0
                    i[2] = int(i[2]/2)
                    i[3] = 2
            elif i[3] == 2:
                i[0] += 1
                if i[0] == n-1 :
                   # i[0] = n-1
                    i[2] = int(i[2]/2)
                    i[3] = 1
            elif i[3] == 3:
                i[1] -= 1
                if i[1] == 0 :
                    #i[1] = 0
                    i[2] = int(i[2]/2)
                    i[3] = 4
            elif i[3] == 4:
                print(i)
                i[1] += 1
                if i[1] == n-1 :
                    i[2] = int(i[2]/2)
                    i[3] == 3
            if not (i[0],i[1]) in xylist :
                xylist.append((i[0],i[1]))
        # print(xylist)
        for j in xylist :
            mymax = 0
            mysum = 0
            myside = 0
            for t in item :
                if t[2] == 0 :
                    continue
                if t[0] == j[0] and t[1] == j[1] :
                    #print(j,t)
                    mysum += t[2]
                    if mymax < t[2] :
                        mymax = t[2]
                        myside = t[3]
                if j[0] == 0 :
                    myside = 2
                if j[0] == n-1 :
                    myside = 1
                if j[1] == 0 :
                    myside = 4
                if j[1] == n-1 :
                    myside = 3
                else :
                    continue
            #print([j[0],j[1],mysum,myside])
            result.append([j[0],j[1],mysum,myside])
        item = result
    #print(item)
    r = 0
    for i in item :
        r += i[2]
    print(f'#{a+1} {r}')
