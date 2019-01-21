def solve(k,homes,N):
    global result
    count=0
    k=k-1
    for col in range(N):
        for row in range(N):
            tmpcount=0
            for colchange in range(-k,k+1):
                for rowchange in range(-k+abs(colchange),k-abs(colchange)+1):
                        if col+colchange <0 or col+colchange>=N or row+rowchange<0 or row+rowchange>=N:
                            continue
                        else:
                            if homes[col+colchange][row+rowchange]!=0:
                                tmpcount+=1
            if tmpcount>count:
                count=tmpcount
    return count

CS=int(input())
for case in range(CS):
    caseinfo=list(map(int,input().split()))
    homes=[list(map(int,input().split())) for col in range(caseinfo[0])]
    countofHome = 0     #집의 개수의 합
    result = 1
    for onelineOfhomes in homes:
        countofHome+=sum(onelineOfhomes)
    maxofK=1
    while(True):        #집의개수*지불금액이 운영비용보다 작은 시점에 종료하기위한 변수 설정
        operationCost = maxofK**2+(maxofK-1)**2
        if operationCost>caseinfo[1]*countofHome:
            maxofK-=1
            break
        else:
            maxofK+=1
    for k in range(2,maxofK+1):
        count=solve(k,homes,caseinfo[0])
        if (caseinfo[1]*count)-(k**2+(k-1)**2)>=0:
            if count>result:
                result=count
    print(result)
