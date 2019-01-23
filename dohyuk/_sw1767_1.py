def dfs(idx) :
    global item,core,core_max,my,my_min,my_list
    if idx >= len(my_list):
        if core > core_max :
            core_max = core
            my_min = my
        elif core == core_max:
            if my_min > my :
                my_min = my  
        return
    x,y = my_list[idx]
    for j in range(4) :
        if chk(x,y,j) :
            core += 1
            draw(x,y,j,2)
            dfs(idx+1)
            draw(x,y,j,0)
            core -= 1
    dfs(idx+1)
def draw(x,y,pos,ch) :
    global item,core,my
    if pos == 0 :
        for i in range(1,n) :
            if y-i >= 0 :
                if ch == 2 :
                    my += 1
                if ch == 0 :
                    my -= 1
                item[y-i][x] = ch
    if pos == 1 :
        for i in range(1,n) :
            if x+i <n :    
                if ch == 2 :
                    my += 1
                if ch == 0 :
                    my -= 1
                item[y][x+i] = ch
    if pos == 2 :
        for i in range(1,n) :
            if y+i < n :
                if ch == 2 :
                    my += 1
                if ch == 0 :
                    my -= 1
                item[y+i][x] = ch
    if pos == 3 :
        for i in range(1,n) :
            if x-i >= 0 :
                if ch == 2 :
                    my += 1
                if ch == 0 :
                    my -= 1
                item[y][x-i] = ch
def chk(x,y,pos) :
    global item
    if pos == 0 :
        for i in range(1,n) :
            if y-i >= 0 and item[y-i][x] :
                return False
            elif y-i < 0 :
                return True
    if pos == 1 :
        for i in range(1,n) :
            if x+i < n and item[y][x+i] :
                return False
            elif x+i > n  :
                return True
    if pos == 2 :
        for i in range(1,n) :
            if y+i < n and item[y+i][x] :
                return False
            elif y+i > n :
                return True
    if pos == 3 :
        for i in range(1,n) :
            if x-i >= 0 and item[y][x-i] :
                return False
            elif x-i < 0 :
                return True
    return True 
for a in range(int(input())) :
    n = int(input())
    item = [list(map(int,input().split())) for i in range(n)]
    my_list = []
    my_min = 100000
    core = 0
    my = 0
    core_max = -1
    count = 0
    for i in range(1,n-1) :
        for j in range(1,n-1) :
            if item[i][j] > 0 :
                my_list.append((j,i))
    dfs(0)
    print(f'#{a+1} {my_min}')