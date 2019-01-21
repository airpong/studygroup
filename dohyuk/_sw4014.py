def dfs(l,chk,t):
    global x

    if  t >= len(l) - 1 :
        return True
    # if t == len(l)-1:
    #     if l[t] == l[t-1] :
    #         return True
    #     else :
    #         return False
    if l[t] == l[t+1]:
        return dfs(l,chk,t+1)
    # 낮을경우
    elif l[t]  == l[t+1] + 1 :
        if t + x >= len(l) :
            return False
        else :
            for i in range(0,x) :
                if l[t+1] == l[t+1+i] :
                    chk[t+1+i] = 1
                if l[t+1] != l[t+1+i] :
                    return False
            return dfs(l,chk,t+x)
    elif l[t] + 1 == l[t+1] :
        #높을경우
        if t - x + 1 < 0 :
            return False
        else :
            for i in range(0,x) :
                if chk[t-i] :
                    return False
                if l[t] != l[t-i] :
                    return False
                chk[t-i] = 1
            return dfs(l,chk,t+1)

 
        



for a in range(int(input())) :
    m = [] #가로
    k = [] #세로
    chk = [0,0,0,0,0,0]
    n,x = list(map(int,input().split()))
    print(dfs([3, 3, 3, 2, 2, 1],chk,0))
    for t in range(n):
        k.append([])
    for j in range(n) :
        m.append(list(map(int,input().split())))
        for t in range(n) :
            k[t].append(m[j][t])
    result = 0
    for i in m :
        chk = [0 for i in range(n)]
        # if dfs(i,chk,0) :
        #     print(i)
        result += 1 if dfs(i,chk,0) else 0
    for i in k:
        chk = [0 for i in range(n)]
        # if dfs(i,chk,0):
        #     print(i)
        result += 1 if dfs(i,chk,0) else 0
    print(f'#{a+1} {result}')