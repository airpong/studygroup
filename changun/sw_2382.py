



CS=int(input())
for case in range(CS):
    caseinfo = list(map(int,input().split()))
    caseArr = [[0 for j in range(caseinfo[0])] for i in range(caseinfo[0])]
    for k in range(caseinfo[2]):
        association=list(map(int,input().split()))
        caseArr[association[0]][association[1]]=association+[association[2]]
    for time in range(caseinfo[1]):
        tmpcaseArr=[[0 for j in range(caseinfo[0])] for i in range(caseinfo[0])]
        # print("a",tmpcaseArr)
        # tmpcaseArr=[[0]*caseinfo[0]] *caseinfo[0]
        # print("b",arrrf)
        for col in range(len(caseArr)):
            for row in range(len(caseArr[col])):
                if caseArr[col][row]==0:
                    continue
                else:
                    if caseArr[col][row][3]==1:
                        if col-1<=0:
                            caseArr[col][row][2]=caseArr[col][row][2]//2
                            caseArr[col][row][4]=caseArr[col][row][2]
                            caseArr[col][row][3]=2
                        if tmpcaseArr[col-1][row]!=0:
                            tmpcaseArr[col-1][row][2]+=caseArr[col][row][2]
                            if tmpcaseArr[col-1][row][4]<caseArr[col][row][2]:
                                tmpcaseArr[col-1][row][3]=caseArr[col][row][3]
                                tmpcaseArr[col-1][row][4]=caseArr[col][row][2]
                        else:
                            tmpcaseArr[col-1][row]=[caseArr[col][row][0]-1,caseArr[col][row][1],caseArr[col][row][2],caseArr[col][row][3],caseArr[col][row][2]]
                    
                    elif caseArr[col][row][3]==2:
                        if col+1>=caseinfo[0]-1:
                            caseArr[col][row][2]=caseArr[col][row][2]//2
                            caseArr[col][row][4]=caseArr[col][row][2]
                            caseArr[col][row][3]=1
                        if tmpcaseArr[col+1][row]!=0:
                            tmpcaseArr[col+1][row][2]+=caseArr[col][row][2]
                            if tmpcaseArr[col+1][row][4]<caseArr[col][row][2]:
                                tmpcaseArr[col+1][row][3]=caseArr[col][row][3]
                                tmpcaseArr[col+1][row][4]=caseArr[col][row][2]
                        else:
                            tmpcaseArr[col+1][row]=[caseArr[col][row][0]+1,caseArr[col][row][1],caseArr[col][row][2],caseArr[col][row][3],caseArr[col][row][2]]
                    
                    elif caseArr[col][row][3]==3:
                        if row-1<=0:
                            caseArr[col][row][2]=caseArr[col][row][2]//2
                            caseArr[col][row][4]=caseArr[col][row][2]
                            caseArr[col][row][3]=4
                        if tmpcaseArr[col][row-1]!=0:
                            tmpcaseArr[col][row-1][2]+=caseArr[col][row][2]
                            if tmpcaseArr[col][row-1][4]<caseArr[col][row][2]:
                                tmpcaseArr[col][row-1][3]=caseArr[col][row][3]
                                tmpcaseArr[col][row-1][4]=caseArr[col][row][2]
                        else:
                            tmpcaseArr[col][row-1]=[caseArr[col][row][0],caseArr[col][row][1]-1,caseArr[col][row][2],caseArr[col][row][3],caseArr[col][row][2]]

                    elif caseArr[col][row][3]==4:
                        if row+1>=caseinfo[0]-1:
                            caseArr[col][row][2]=caseArr[col][row][2]//2
                            caseArr[col][row][4]=caseArr[col][row][2]
                            caseArr[col][row][3]=3
                        if tmpcaseArr[col][row+1]!=0:
                            tmpcaseArr[col][row+1][2]+=caseArr[col][row][2]
                            if tmpcaseArr[col][row+1][4]<caseArr[col][row][2]:
                                tmpcaseArr[col][row+1][3]=caseArr[col][row][3]
                                tmpcaseArr[col][row+1][4]=caseArr[col][row][2]
                        else:
                            tmpcaseArr[col][row+1]=[caseArr[col][row][0],caseArr[col][row][1]+1,caseArr[col][row][2],caseArr[col][row][3],caseArr[col][row][2]]
        caseArr=tmpcaseArr
    print(caseArr)
    Sum=0
    for col in range(caseinfo[0]):
        for row in range(caseinfo[0]):
            if caseArr[col][row]!=0:
                Sum+=caseArr[col][row][2]
    print(Sum)