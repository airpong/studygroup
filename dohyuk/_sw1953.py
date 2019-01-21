def dfs(pos,now_x,now_y) :
    global n,m,x,y,status,allmap
    if pos > time :
        return
    item = allmap[now_y][now_x]
    side_item = [0,0,0,0]
    if now_y - 1 >= 0 :
        side_item[0] = (now_y-1,now_x)
    if now_x + 1 < m :
        side_item[1] = (now_y,now_x+1)  
    if now_y + 1 < n :
        side_item[2] = (now_y+1,now_x)
    if now_x -1 >= 0:
        side_item[3] = (now_y,now_x-1)
    if not (now_x,now_y) in status :
        status.append((now_x,now_y))
    allowlist = [0,[0,1,2,3],[0,2],[1,3],[0,1],[1,2],[2,3],[0,3]]
    gotolist = [[1,2,5,6],[1,3,6,7],[1,2,4,7],[1,3,4,5]]
    for i in allowlist[item] :
        if side_item[i] :
            if allmap[side_item[i][0]][side_item[i][1]] in gotolist[i] :
                allmap[now_y][now_x] = 0
                x1 = side_item[i][1]
                y1 = side_item[i][0]
                dfs(pos+1,x1,y1)
                allmap[now_y][now_x] = item
        

for a in range(int(input())) :
    n,m,y,x,time = list(map(int,input().split()))
    allmap = [list(map(int,input().split())) for i in range(n)]
    status = []
    dfs(1,x,y)
    print(f'#{a+1} {len(status)}')
