for T in range(int(input())):
    n,m,k=list(map(int,input().split()))
    case=[]
    counting=0
    for column in range(n):
        row=list(map(int,input().split()))
        case_row=[]
        for row2 in range(m):
            case_row.append([row[row2],0])
            if row[row2]!=0:
                counting+=1
        case.append(case_row)
    # 최대 700*700 리스트 만들기(안 터지나?)
    for row in case:
        for i in range(k):
            row.insert(0,[0,0])
            row.insert(len(row),[0,0])
    for i in range(k):
        case.insert(0,[[0,0] for j in range(len(row))])
        case.insert(len(case),[[0,0] for k in range(len(row))])
    for time in range(1,k+1):
        print(time,end=' ')
        for column in range(len(case)):
            for row in range(len(case[0])):
                target=case[column][row]
                if target[0]!=-1:
                    # 분열시키기
                    if time-target[1]==target[0]+1 and target[0]!=0:
                        print(target[0],end='')
                        if case[column-1][row][0]==0:
                            case[column-1][row][0]=target[0]
                            case[column-1][row][1]=time
                            counting+=1
                        if case[column+1][row][0]==0:
                            case[column+1][row][0]=target[0]
                            case[column+1][row][1]=time
                            counting+=1
                        if case[column][row+1][0]==0:
                            case[column][row+1][0]=target[0]
                            case[column][row+1][1]=time
                            counting+=1
                        if case[column][row-1][0]==0:
                            case[column][row-1][0]=target[0]
                            case[column][row-1][1]=time
                            counting+=1
                        if case[column-1][row][1]==time:
                            if case[column-1][row][0]<target[0]:
                                case[column-1][row][0]=target[0]
                                case[column-1][row][1]=time
                        if case[column+1][row][1]==time:
                            if case[column+1][row][0]<target[0]:
                                case[column+1][row][0]=target[0]
                                case[column+1][row][1]=time
                        if case[column][row+1][1]==time:
                            if case[column][row+1][0]<target[0]:
                                case[column][row+1][0]=target[0]
                                case[column][row+1][1]=time
                        if case[column][row-1][1]==time:
                            if case[column][row-1][0]<target[0]:
                                case[column][row-1][0]=target[0]
                                case[column][row-1][1]=time
                    # 죽이기
                    if target[0]!=0:
                        if time-target[1]==target[0]*2:
                            target[0]=-1
                            counting-=1
        print()
    print(f'#{T+1} {counting}')