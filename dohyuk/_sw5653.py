for a in range(int(input())) :
    n,m,k = list(map(int,input().split()))
    item = [list(map(int,input().split())) for i in range(n)]
    my_map = {}
    result = 0
    time = 0
    for i,l in enumerate(item) :
        for j,t in enumerate(l) :
            if item[i][j] > 0 :
                my_map[(j,i)] =(item[i][j],item[i][j]*2)
    
    while time < k :
        tempdic = {}
        #print(time,len(my_map))
        for key,value in my_map.items() :
            if value[0] > 0:
                if value[0] == value[1] :
                    for i in range(-1,2,2) :
                        x,y = key
                        if not my_map.get((x+i, y)) :
                            if tempdic.get((x+i, y)) :
                                if value[0] > tempdic.get((x+i, y))[0] :
                                    tempdic.update({(x+i,y) : (value[0], value[0]*2)})
                            else :
                                tempdic.update({(x+i,y) : (value[0], value[0]*2)})    
                        if not my_map.get((x, y+i)) :
                            if tempdic.get((x, y+i)) :
                                if value[0] > tempdic.get((x, y+i))[0] :
                                    tempdic.update({(x,y+i) : (value[0], value[0]*2)})
                            else :
                                tempdic.update({(x,y+i) : (value[0], value[0]*2)})
        for key,value in my_map.items() :
            my_map[key] = (value[0],value[1]-1)
        if tempdic :
            my_map.update(tempdic)
        time += 1
    for key,value in my_map.items() :
        if value[0] > 0 and value[1] > 0 :
            result += 1
    print(f'#{a+1} {result}')