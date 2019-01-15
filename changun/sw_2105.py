def DFS(column,row,lst,endC,endR,dirt,a):
    global Maxresult
    global n
    global caseinput
    global direction
    if column>=n or row>=n or column<0 or row<0:
        return
    elif caseinput[column][row] in lst:
        return
    elif column == endC and row == endR:
        lst.append(caseinput[column][row])
        if len(lst)>Maxresult:
            Maxresult=len(lst)

    else:
        
        lst.append(caseinput[column][row])
        for i in range(2):
            tmplst=lst.copy()
            if dirt+i >=4:
                goto=0
            else:
                goto=dirt+i
            if i==1 and a==0:
                break
            if endC-column == row-endR and endC-column>0 and dirt==2 and i==0:
                continue
            DFS(column+direction[goto][0],row+direction[goto][1],tmplst,endC,endR,goto,1)

direction = [(1,1),(-1,1),(-1,-1),(1,-1)]
casesize = int(input())
for i in range(casesize):
    Maxresult = -1
    n = int(input())
    caseinput=[list(map(int,input().split())) for line in range(n)]
    for column in range(1,n-1):
        for row in range(n-2):
            lst=[]
            a=0
            DFS(column,row,lst,column-1,row+1,0,a)
    print(f'#{i+1} {Maxresult}')