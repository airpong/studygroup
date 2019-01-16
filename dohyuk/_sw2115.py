def score(item,c) :
    result = 0
    if sum(item) > c :
        my_max = 0
        temp = 0
        if len(item) <= 2 :
            result = max(item)**2
            return result
        else:
            n = len(item)
            for i in range(2**n) :
                st = bin(i)[2:].zfill(n)
                #print(st)
                temp = 0
                result = 0
                for j in range(len(st)) :
                    if st[j] == '1':
                        temp += item[j]
                        result += item[j]**2
                if temp > c :
                    continue
                                            
                if my_max < result :
                    my_max = result
            result = my_max
    else :
        for s in item:
            result += s**2
    return result
for a in range(int(input())) :
    n,m,c = list(map(int,input().split()))
    l=[list(map(int,input().split())) for i in range(n)]
    my_max = 0
    fst = []
    sed = []
    for i in range(n) :
        for j in range(i,n) :
            fst.clear()
            for k in range(0,n-m+1) :
                fst = l[i][k:k+m]
                sed.clear()
                p = 0
                if i == j :
                    p = k+m
                for t in range(p,n-m+1) :
                    result = 0
                    sed = l[j][t:t+m]
                    result += score(fst,c) + score(sed,c)
                    # print(fst, sed,result)
                    # print(score(fst,c),score(sed,c))
                    if my_max < result :
                        my_max = result                
    print(f'#{a+1} {my_max}')