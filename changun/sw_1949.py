import copy
def DFS(x,y,N,array,pos,flag):
    global Maxdistance
    global K
    tmp=0
    
    for i in range(-1,2,2):
        if x+i >= 0 and x+i <N :
            if array[x+i][y] < array[x][y]:
                tmparray=copy.deepcopy(array)
                tmparray[x][y]=100
                DFS(x+i,y,N,tmparray,pos+1,flag)
                tmp=1
            else :
                if flag==1:
                    if array[x+i][y]-array[x][y]<K:
                        tmp=1
                        tmparray=copy.deepcopy(array)
                        tmparray[x+i][y]=tmparray[x][y]-1
                        DFS(x+i,y,N,tmparray,pos+1,0)
        if y+i >= 0 and y+i <N :
            if array[x][y+i] < array[x][y]:
                tmparray=copy.deepcopy(array)
                tmparray[x][y]=100
                DFS(x,y+i,N,tmparray,pos+1,flag)
                tmp=1
            else :
                if flag==1:
                    if array[x][y+i]-array[x][y]<K:
                        tmp=1
                        tmparray=copy.deepcopy(array)
                        tmparray[x][y+i]=tmparray[x][y]-1
                        DFS(x,y+i,N,tmparray,pos+1,0)
    if tmp==0:
        if pos>Maxdistance:
            Maxdistance=pos
        

CS=int(input())
for case in range(CS):
    caseinfo=list(map(int,input().split()))
    caseArr = [list(map(int,input().split())) for i in range(caseinfo[0])]
    startpoint = []
    Max=0
    Maxdistance=0
    K=caseinfo[1]
    for i in range(caseinfo[0]):
        for j in range(caseinfo[0]):
            if caseArr[i][j]>Max:
                startpoint=[[i,j]]
                Max=caseArr[i][j]
            elif caseArr[i][j]==Max:
                startpoint.append([i,j])
    for i in startpoint:
        DFS(i[0],i[1],caseinfo[0],caseArr,1,1)
    print(Maxdistance)
    