def dfs(x,y,pos,my_list) :
    global item,core,core_max,my,my_min,count
    temp_list = my_list[:]
    temp_list.remove((x,y))
#    print(temp_list,x,y)
    count += 1
    draw(x,y,pos,2)
    for i in temp_list:
        x1,y1 = i
        for j in range(4) :
            if chk(x1,y1,j) :
                dfs(x1,y1,j,temp_list)
    # if core == 5 and my == 16:
    #     for t in item :
    #         print(t)
    #     print('cc')
    if core >= core_max :
        core_max = core
        if my_min > my :
            my_min = my       
    draw(x,y,pos,0)
    return

        
def draw(x,y,pos,ch) :
    global item,core,my
    if ch == 2 :
        core += 1
    if ch == 0 :
        core -= 1
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
            #print(item[y-i][x])
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
    core_max = 0
    count = 0
    for i in range(1,n-1) :
        for j in range(1,n-1) :
            if item[i][j] > 0 :
                my_list.append((j,i))
    for i in my_list :
        x,y = i
        for j in range(4) :
            if chk(x,y,j) :
                dfs(x,y,j,my_list)
        break
                #print(my)
                
    # my = 0
    # my_min = 1000000
    # for i in my_list :
    #     x,y = i
    #     for j in range(4) :
    #         if chk(x,y,j) :
    #             my = 0
    #             dfs(x,y,j,my_list)
    # for j in range(4) :
    #     print(1,4,j)
    #     if chk(2,1,j) :
    #         for t in item :
    #             print(t)
    #         print(chk(2,1,j))
    #         draw(2,1,j,2)
    #         for t in item :
    #             print(t)
    #         draw(2,1,j,0)
    print(my_min,core_max)
    print(count)
