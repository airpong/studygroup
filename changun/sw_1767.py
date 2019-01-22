import copy
def DFS(Arr,lst,idx,N,core,distance):
    global maxnode
    global mindistance
    flag=0
    if not lst:
        pass
    else:    
        for direction in range(4):
            tmpArr=copy.deepcopy(Arr)
            connectResult=connectline(tmpArr,lst[idx],direction,N,distance)
            if connectResult[0]:
                distance=connectResult[1]
                core+=1
                flag=1
                tmplst=copy.deepcopy(lst)
                del tmplst[idx]
                for i in range(len(tmplst)):
                    tmptmplst=copy.deepcopy(tmplst)
                    DFS(tmpArr,tmptmplst,i,N,core,distance)
    if flag==0:
        if core>=maxnode:
            if distance<mindistance:
                maxnode=core
                mindistance=distance

def connectline(arr,lst,direction,N,distance):
    if direction==0:
        count=0
        for i in range(lst[0]):
            if arr[i][lst[1]]==0:
                arr[i][lst[1]]=-1
                count+=1
                continue
            else:
                return False,distance
    elif direction==1:
        count=0
        for i in range(lst[1]+1,N):
            if arr[lst[0]][i]==0:
                arr[lst[0]][i]=-1
                count+=1
                continue
            else:
                return False,distance
    elif direction==2:
        count=0
        for i in range(lst[0]+1,N):
            if arr[i][lst[1]]==0:
                arr[i][lst[1]]=-1
                count+=1
                continue
            else:
                return False,distance
    elif direction==3:
        count=0
        for i in range(lst[1]):
            if arr[lst[0]][i]==0:
                arr[lst[0]][i]=-1
                count+=1
                continue
            else:
                return False,distance
    return (True, distance+count)

CS = int(input())
for case in range(CS):  
    lst = []
    maxnode=0
    mindistance=1000
    caseinfo=int(input())
    caseArr=[list(map(int,input().split())) for i in range(caseinfo)]
    for i in range(1,caseinfo):
        for j in range(1,caseinfo):
            if caseArr[i][j]==1:
                lst.append([i,j])
    print(lst)
    for idx in range(len(lst)):
        DFS(caseArr,lst,idx,caseinfo,0,0)
    print(mindistance)