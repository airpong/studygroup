def move(person, side) :
    if side == 0:
        return person
    elif side == 1:
        return (person[0],person[1]-1)
    elif side == 2:
        return (person[0]+1,person[1])
    elif side == 3:
        return (person[0],person[1]+1)
    elif side == 4:
        return (person[0]-1,person[1])
for a in range(int(input())) :
    M,A = list(map(int,input().split()))
    ListA = [0]+list(map(int,input().split()))
    ListB = [0]+list(map(int,input().split()))
    personA = (1,1)
    personB = (10,10)
    bcList = []
    for i in range(A):
        x,y,charge,power = list(map(int,input().split()))
        bcList.append([i,x,y,charge,power])
    sumA =sumB = 0
    for i in range(M+1):
        personA = move(personA,ListA[i])
        personB = move(personB,ListB[i])
        x1,y1 = personA
        x2,y2 = personB
        itemA=bcA=itemB=bcB = -1
        tempA = []
        tempB = []
        for k in bcList :
            if abs(x1-k[1]) + abs(y1-k[2]) <= k[3] :
                tempA.append((k[4],k[0]))
                if itemA < k[4] :
                    itemA = k[4]
                    bcA = k[0]
            if abs(x2-k[1]) + abs(y2-k[2]) <= k[3] :
                tempB.append((k[4],k[0]))
                if itemB < k[4] :
                    itemB = k[4]
                    bcB = k[0]
        if bcA == -1 and bcB == -1 :
            continue
        if bcA == bcB :
            if len(tempA) == 1 and len(tempB) == 1 :
                sumA += itemA//2
                sumB += itemB//2
            else :
                plus = 0
                for k,p in tempA :
                    for k1,p1 in tempB :
                        if not k + k1 == itemA + itemB :
                            if k+k1 > plus :
                                plus = k+k1
                sumA += plus
                #sumB += itemB
        else :
            if itemA > 0:
                sumA += itemA
            if itemB > 0 :
                sumB += itemB
        # print(i,personA,itemA,bcA,personB,itemB,bcB)
        # print(sumA, sumB)
    print(f'#{a+1} {sumA+sumB}')
    

