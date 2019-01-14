def Bomb(x,y,n,W,H,brick):
    if x<0 or x>=W or y<0 or y>=H:
        return
    else:
        if n==0:
            return
        elif n==1:  #1이면 한번 더 불러도 되는데 수행복잡도 때문에 조건 걸어줌
            brick[x][y]=0
            return
        else:    
            brick[x][y] = 0
            for i in range(1-n,n):
                DFS(x,y+i,brick[x][y+i],W,H)
                DFS(x+i,y,brick[x+i][y],W,H)
def DFS(pos,array):
    global Minresult
    if pos>2:
        count=0
        for oneline in len(array):
            for j in oneline:
                count+=1
        if count<Minresult:
            Minresult=count
    else:
        for i in range(array):
            pos+=1
            Bomb()
            DFS(pos)
casesize=int(input())
for case in range(casesize):
    bricks=[]
    caseinfo = list(map(int,input().split()))
    for brick in range(caseinfo[1]):
        bricks.append([])
    for i in range(caseinfo[2]):
        brick=list(map(int,input().split()))
        for j in range(len(brick)):
            if brick[j]!=0:
                bricks[j].append(brick[j])      #열로 값을 전환하여 저장
    print(bricks)
    originalBricks = bricks.copy()
    for i in range (caseinfo[1]):
        for ball in rnage( [0]):
            Hs=[len(bricks[height])-1 for height in len(bricks)] 
            n=bricks[i][Hs[i]]
            DFS(i,Hs[x],n,len(Hs),Hs[x]+1)
            for aaa:    #터진것은 없애주자.
                pass

    # for ball in range(caseinfo[0]):     #공 떨어트리기 시작
    #     Hs=[len(brick[height])-1 for height in len(bricks)]     
    #     for x in range(len(Hs)):
    #         n=brick[x][Hs[x]]
    #         DFS(x,Hs[x],n,len(Hs),Hs[x]+1)
    #         for i in range(caseinfo[1]):
    #             pass