def caseinput(caseArr,startArr,x,y,k,candidate):        #최종배열에 초기배열 반영 함수
    for i in range(k,k+x):
        for j in range(k,k+y):
            caseArr[i][j]=[startArr[i-k][j-k],startArr[i-k][j-k],1]
            if caseArr[i][j][0]!=0:
                candidate.append([i,j])

def solve(candidate,caseArr,tmpcandidate,tmpdeleted):      #후보군 검사+확장을 포함하는 함수
    for i in range(len(candidate)):
        Isdeleted=check(candidate[i],caseArr,tmpcandidate)
        if Isdeleted:
            tmpdeleted.append(i)

def check(candidate,caseArr,tmpcandidate):      #후보군(int1,int2,flag) 검사/flag가 2일경우 확장/int1이 0이 될경우(활성상태 될경우) flag 2로 변경/int2가 0이 될경우(활성상태 끝날경우) 후보군에서 삭제
    ckx=candidate[0]
    cky=candidate[1]
    result=False
    if caseArr[ckx][cky][2]==2:
        life=caseArr[ckx][cky][1]
        caseArr[ckx][cky][2]=1
        caseArr[ckx][cky][1]-=1
        expand(ckx,cky,life,caseArr,tmpcandidate)
    elif caseArr[ckx][cky][0]>0:
        caseArr[ckx][cky][0]-=1
        if caseArr[ckx][cky][0]==0:
            caseArr[ckx][cky][2]=2
    elif caseArr[ckx][cky][1]>0:
        caseArr[ckx][cky][1]-=1
        if caseArr[ckx][cky][1]==0:
            caseArr[ckx][cky][2]=0
            result = True
    return result

def expand(x,y,life,caseArr,tmpcandidate):      #확장 시키는 함수. flag=0이면 진행/배열의 원소값이 (0,0,1)이면 확장후 후보군에 저장/후보군에 있을경우 비교후 저장
    for col in range(-1,2,2):
        if caseArr[x+col][y][2]==0:
            continue
        elif caseArr[x+col][y][0]==0 and caseArr[x+col][y][1]==0:
            caseArr[x+col][y]=[life,life,1]
            tmpcandidate.append([x+col,y,1])
        elif (x+col,y,1) in tmpcandidate:
            if life>caseArr[x+col][y][0]:
                caseArr[x+col][y]=[life,life,1]
    for row in range(-1,2,2):
        if caseArr[x][y+row][2]==0:
            continue
        elif caseArr[x][y+row][0]==0 and caseArr[x][y+row][1]==0:
            caseArr[x][y+row]=(life,life,1)
            tmpcandidate.append((x,y+row,1))
        elif (x,y+row,1) in tmpcandidate:
            if life>caseArr[x][y+row][0]:
                caseArr[x][y+row]=(life,life,1)



CS=int(input())
for case in range(CS):
    caseinfo = list(map(int,input().split()))       #caseinfo = [세로,가로,반복횟수]
    startArr = [list(map(int,input().split())) for i in range(caseinfo[0])]     #초기 시작 배열
    caseArr = [[[0,0,1] for i in range((2*caseinfo[2]+caseinfo[0]))] for i in range(2*caseinfo[2]+caseinfo[1])]       #시행횟수를 고려한 충분히 큰 최종 배열 각 위치에 (생명력수치,생명력수치,flag) 가 들어가게 된다.
    candidate = []      #활성+비활성 세포의 집합
    caseinput(caseArr,startArr,caseinfo[0],caseinfo[1],caseinfo[2],candidate)        
    for i in range(caseinfo[2]):
        tmpcandidate = []
        tmpdeleted = []
        solve(candidate,caseArr,tmpcandidate,tmpdeleted)
        candidate+tmpcandidate
        for deleted in tmpdeleted:
            del candidate[deleted]
        candidate=candidate+tmpcandidate