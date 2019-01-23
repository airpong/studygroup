def dfs(x,y,drt) :
    global max_score,crush,item,n
    global m_x, m_y, hole
    # if (now == -1 or (x == m_x and y == m_y)) and drt != -1 :
    #     if score > max_score :
    #         max_score = score
    #     return
    score = 0
    stop = True
    k = 0
    while stop :
        # k+= 1
        # print(x,y)
        now = item[y][x]
        if now == -1 or (x == m_x and y == m_y) :
            if score > max_score :
                max_score = score
            stop = False
            break
        if now == 0 :
            if drt == 0 :
                for i in range(n+2) :
                    if y-i >= 0 :
                        if item[y-i][x] != 0 :
                            break
                        if y-i == m_y and x == m_x :
                            if score > max_score :
                                max_score = score
                            stop = False
                            break
                y = y-i
            if drt == 1 :
                for i in range(n+2) :
                    if x+i < n+2 :
                        if item[y][x+i] != 0:
                            break
                        if y == m_y and x+i == m_x :
                            if score > max_score :
                                max_score = score
                            stop = False
                            break
                x = x+i
            if drt == 2 :
                for i in range(n+2) :
                    if y+i < n+2 :
                        if item[y+i][x] != 0:
                            break
                        if y+i == m_y and x == m_x :
                            if score > max_score :
                                max_score = score
                            stop = False
                            break    
                y = y+i
            if drt == 3 :
                for i in range(n+2) :
                    if x-i >= 0 :
                        if item[y][x-i] != 0:
                            break
                        if y == m_y and x-i == m_x :
                            if score > max_score :
                                max_score = score
                            stop = False
                            break
                x = x-i
        if now > 0 and now < 6 :
            score += 1
            drt = crush[now-1][drt]
            if drt == 0 :
                y = y-1
            if drt == 1 :
                x = x+1
            if drt == 2 :
                y = y+1
            if drt == 3 :
                x = x-1
        if now > 5 :
            for key,value in hole.items() :
                if key != (x,y) and now == value:
                    i,j = key
                    if drt == 0 :
                        x=i
                        y=j-1
                    if drt == 1 :
                        x=i+1
                        y=j
                    if drt == 2 :
                        x=i
                        y=j+1
                    if drt == 3 :
                        x=i-1
                        y=j
                    break
    if score > max_score :
        max_score = score
    return

for a in range(int(input())) :
    n = int(input())
    item = [list(map(int,input().split())) for i in range(n)]
    max_score = -1
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
    for i in range(n+2) :
        for j in range(n+2) :
            if item[i][j] == 0 :
                m_x = j
                m_y = i
                dfs(j,i-1,0)
                dfs(j+1,i,1)
                dfs(j,i+1,2)
                dfs(j-1,i,3)
    # m_x = 4
    # m_y = 3
    # score = 0
    # dfs(5,3,1)
    print(f'#{a+1} {max_score}')