def timec(bincase,person,floor,floorList) :
    time = 0
    AList , BList = floorList[0] , floorList[1]
    A,B=floor[0],floor[1]
    state = []
    for i in range(len(bincase)) :
        if bincase[i] == '1':
            state.append(abs(A[0] - person[i][0]) + abs(A[1] - person[i][1])+1)  #대기시간 1분까지 더해줌
        else :
            state.append(abs(B[0] - person[i][0]) + abs(B[1] - person[i][1])+1) #대기시간 1분까지 더해줌
    #print(state)
    fin = len(state) + len(AList) + len(BList)
    chkfin = 0
    while chkfin < fin :
        # if bincase == '1111111':
        #     print(time,state,AList,BList)
        #break 주기
        chkfin = 0
        for i in state :
            if i == -1 :
                chkfin += 1
        for i in AList :
            if i == 0 :
                chkfin += 1
        for i in BList :
            if i == 0 :
                chkfin += 1
        if chkfin >= fin :
            break
        for i in range(len(state)) :
            if state[i] > 0 :
                state[i] -= 1
        # 0 이상이면 한개씩줄여주고
        
        if 0 in state :
            checkA = checkB = 0
            del AList[0]
            del BList[0]
            time += 1
            for i in range(len(state)) :
                if state[i] == 0 :
                    if bincase[i] == '1':
                        if sum(AList) + checkA < 3 :
                            state[i] = -1
                            checkA+=1
                        else :
                            continue
                    else :
                        if sum(BList) + checkB < 3 :
                            state[i] = -1
                            checkB+=1
                        else :
                            continue
            # AList.insert(len(AList)-1,checkA)
            # del AList[0]
            # BList.insert(len(BList)-1,checkB)
            # del BList[0]
            AList.append(checkA)
            BList.append(checkB)
            continue
        else :
            AList.append(0)
            del AList[0]
            BList.append(0)
            del BList[0]
            #0이 없으면 통로에 0을 추가해주고 맨앞을 제거
        time += 1
    return time
for a in range(int(input())):
    n =int(input())
    allmap=[list(map(int,input().split())) for i in range(n)]
    # person = [(x,y) for x in range(n) for y in range(n) if allmap[x][y]==1]
    # floor = [(x,y) for x in range(n) for y in range(n) if allmap[x][y] > 1]
    # 사람위치,계단 리스트 추가
    person = []
    floorList = []
    floor = []
    for x in range(n) :
        for y in range(n) :
            temp = allmap[x][y]
            if temp == 1 :
                person.append((x,y))
            elif temp > 1 :
                floorList.append([0 for i in range(temp)])
                floor.append((x,y))
    #==               
    t = 2**len(person)
    m = k = -1
    for i in range(t) :
        k = timec(bin(i)[2:].zfill(len(person)),person,floor,floorList)
        #print(bin(i)[2:].zfill(len(person)),k)
        if m >= k:
            m = k
    print(f'#{a+1} {m{')
