def solve(height,caseinput,gill):
    global caseresult
    # print(caseinput)
    for i in range(height):
        result = 0
        Maxofcol = max(caseinput[i])
        tmpN=-1
        Sum=0
        j=-1
        while(j<(len(caseinput[i])-1)):
            j+=1
            nownum=caseinput[i][j]
            if tmpN==-1:
                tmpN=nownum
                Sum+=nownum
                # print('a',nownum,Sum)
            elif nownum==Maxofcol and tmpN==Maxofcol:
                tmpN=nownum
                Sum=0
                # print('b',nownum,Sum)
                continue
            elif nownum==tmpN :
                Sum+=nownum
                # print('c',j,tmpN)
                continue
            elif nownum>tmpN:
                if nownum-tmpN != 1:
                    result=-1
                    # print('d')
                    break
                else:
                    if Sum>=gill*tmpN:
                        Sum=nownum
                        tmpN=nownum
                        # print('e',Sum,gill,tmpN)
                    else:
                        result=-1
                        # print('f')
                        break
            elif nownum<tmpN:
                if nownum-tmpN!=-1:
                    result=-1
                    # print('g')
                    break
                else:
                    Sum=nownum
                    for k in range(j+1,j+gill):
                        if k>=len(caseinput[i]):
                            break
                        if caseinput[i][k]!=nownum:
                            # print('h',k,j,Sum)
                            break
                        else :
                            Sum+=nownum
                            # print('z',k,j,Sum)
                    if Sum>=gill*nownum:
                        # print('I',k,j)
                        tmpN=nownum
                        Sum=0
                        j=j+gill-1
                        # print(j,Sum)
                    else:
                        # print('J',k,j)
                        result=-1
                        break
        if result==0:
            # print("bammm",i,j)
            caseresult+=1
            
casesize = int(input())
for i in range(casesize):
    caseresult=0
    caseinfo=list(map(int,input().split()))
    rowArray=[[] for i in range(caseinfo[0])]
    colArray=[]
    for j in range(caseinfo[0]):
        lines=list(map(int,input().split()))
        colArray.append(lines)
        for k in range(caseinfo[0]):
            rowArray[k].append(lines[k])
    solve(caseinfo[0],rowArray,caseinfo[1])
    solve(caseinfo[0],colArray,caseinfo[1])
    print(f'#{i+1} {caseresult}')
    