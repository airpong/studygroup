def dfs(x,y,drt) :
    global max_score,score,crush,item,n
    global m_x, m_y, hole
    now = item[y][x]
    # print(x,y)
    if (now == -1 or (x == m_x and y == m_y)) and drt != -1 :
        if score > max_score :
            max_score = score
        return
    if drt == -1:
        score = 0
        dfs(x,y-1,0)
        score = 0
        dfs(x+1,y,1)
        score = 0
        dfs(x,y+1,2)
        score = 0
        dfs(x-1,y,3)

    if now == 0 :
        if drt == 0 :
            for i in range(n+2) :
                if y-i >= 0 :
                    if item[y-i][x] != 0 :
                        break
                    if y-i == m_y and x == m_x :
                        if score > max_score :
                            max_score = score
                        return
            dfs(x,y-i,drt)
        if drt == 1 :
            for i in range(n+2) :
                if x+i < n+2 :
                    if item[y][x+i] != 0:
                        break
                    if y == m_y and x+i == m_x :
                        if score > max_score :
                            max_score = score
                        return
            dfs(x+i,y,drt)
        if drt == 2 :
            for i in range(n+2) :
                if y+i < n+2 :
                    if item[y+i][x] != 0:
                        break
                    if y+i == m_y and x == m_x :
                        if score > max_score :
                            max_score = score
                        return    
            dfs(x,y+i,drt)
        if drt == 3 :
            for i in range(n+2) :
                if x-i >= 0 :
                    if item[y][x-i] != 0:
                        break
                    if y == m_y and x-i == m_x :
                        if score > max_score :
                            max_score = score
                        return
            dfs(x-i,y,drt)
    if now > 0 and now < 6 :
        score += 1
        nextdir = crush[now-1][drt]
        if nextdir == 0 :
            dfs(x,y-1,nextdir)
        if nextdir == 1 :
            dfs(x+1,y,nextdir)
        if nextdir == 2 :
            dfs(x,y+1,nextdir)
        if nextdir == 3 :
            dfs(x-1,y,nextdir)
    if now > 5 :
        for key,value in hole.items() :
            if key != (x,y) and now == value:
                i,j = key
                if drt == 0 :
                    dfs(i,j-1,drt)
                if drt == 1 :
                    dfs(i+1,j,drt)
                if drt == 2 :
                    dfs(i,j+1,drt)
                if drt == 3 :
                    dfs(i-1,j,drt)
    return

for a in range(int(input())) :
    n = int(input())
    item = [list(map(int,input().split())) for i in range(n)]
    max_score = 0
    wall = [5 for i in range(n)]
    item.insert(0,wall[:])
    item.append(wall[:])
    for i in item :
        i.insert(0,5)
        i.append(5)
    crush = [
        [2,3,1,0],[1,3,0,2],[3,2,0,1],[2,0,3,1],[2,3,0,1]
    ]
    hole = {}
    for i in range(n+2) :
        for j in range(n+2) :
            if item[i][j] > 5 :
                hole[(j,i)] = item[i][j]
    # print(hole)
    for i in range(n+2) :
        for j in range(n+2) :
            if item[i][j] == 0 :
                m_x = j
                m_y = i
                score = 0
                dfs(j,i,-1)
            

    # m_x = 4
    # m_y = 3
    # score = 0
    # dfs(4,3,-1)
    print(f'#{a+1} {max_score}')