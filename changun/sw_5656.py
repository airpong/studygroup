import copy
def Bomb(x,y,brick,pos):
    W=len(brick)
    if x<0 or x>=W :
        return
    H=len(brick[x])
    if H==0:
        return
    if y<0 or y>=H:
        return
    n=brick[x][y]
    if n==0:
        return
    elif n==1:  #1이면 한번 더 불러도 되는데 수행복잡도 때문에 조건 걸어줌
        brick[x][y]=0
        return
    else:   
        brick[x][y] = 0
        for i in range(1-n,n):
            Bomb(x,y+i,brick,pos)
            Bomb(x+i,y,brick,pos)
def DFS(n,start,brick,pos):
    global Minresult
    if pos>=n:
        count=0
        for oneline in brick:
            count+=len(oneline)
        if count<Minresult:
            Minresult=count
    else:
        x=start
        y=len(brick[x])-1
        Bomb(x,y,brick,pos)
        i=0
        while(i<=len(brick)-1):
            j=0
            while(j<=len(brick[i])-1):
                if brick[i][j]==0:
                    del brick[i][j]
                    j-=1
                j+=1
            i+=1
        # print("afterbrick",brick)
        for i in range(len(brick)):
            tmpbrick=copy.deepcopy(brick)
            pos+=1
            DFS(n,i,tmpbrick,pos)
            pos-=1
casesize=int(input())
for case in range(casesize):
    Minresult=100000
    bricks=[]
    caseinfo = list(map(int,input().split()))
    for brick in range(caseinfo[1]):
        bricks.append([])
    for i in range(caseinfo[2]):
        brick=list(map(int,input().split()))
        for j in range(len(brick)):
            if brick[j]!=0:
                bricks[j]=[brick[j]]+bricks[j]
                      #열로 값을 전환하여 저장
    for i in range(len(bricks)):
        runbricks = copy.deepcopy(bricks)
        DFS(caseinfo[0],i,runbricks,0)
    print('#',case+1,' ',Minresult,sep="")