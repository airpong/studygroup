import sys
casesize = int(input())
manlocation = []
floirlocantion = []
howcase = []
mapsize=0
howmanypeople = 0

def inputcase():    #사람위치,계단 위치 입력받는 함수
    global manlocation    #사람 위치 (x,y) 로 리스트에 저장
    manlocation = []
    # print("사람위치 초기화 확인  ",manlocation)
    global floirlocantion #계단 위치 (x,y,z) 로 리스트에 저장 z는 시간
    floirlocantion = []
    global mapsize
    mapsize= int(input())
    global howmanypeople
    for i in range(mapsize): 
        line=input().split()
        for j in range(mapsize):
            if(int(line[j])==1):
                manlocation.append([i,j,'0'])
                howcase.append(0)
            elif(int(line[j])!=0):
                floirlocantion.append([i,j,int(line[j])])
    howmanypeople = len(manlocation)

def solve():
    global howcase
    howcase=list(howcase.zfill(len(manlocation)))
    # print(f'이번 케이스는 {howcase}')
    attimeA = [0 for i in range(100)]   #계단 A의 100분 까지 시간, 각 요소는 분에 해당하고 해당분에 계단을 몇명이 이용했는지 알수있다.
    attimeB = [0 for i in range(100)]
    # print(f'타임 초기화 되었는지 확인 {attimeA}')
    afloir = []     #A계단에 할당받은 사람들의 거리를 저장
    bfloir = []
    floirtime = 0      #계단별 이동시간을 비교하기 위한 변수
    for idx in (range(len(manlocation))):
        manlocation[idx][2]=howcase[idx]
    # print("사람들은 어디 계단으로 갔는지 ",manlocation)
    # print(f'계단 확인 {floirlocantion}')
    for man in manlocation:     #계단으로 할당된 사람들의 계단과의 거리를 구함
        if man[2]=='0':
            afloir.append(abs(man[0]-floirlocantion[0][0])+abs(man[1]-floirlocantion[0][1])+1)     #A계단과의 거리
        else :
            bfloir.append(abs(man[0]-floirlocantion[1][0])+abs(man[1]-floirlocantion[1][1])+1)     #B계단과의 거리
    # print(f'floA {afloir} flob {bfloir}')
    afloir.sort()     #계단과의 거리순 정렬
    bfloir.sort()
    # print(f'Sorted floA {afloir} flob {bfloir}')
    for a in afloir:
        move(attimeA,a,floirlocantion[0][2])
    for b in bfloir:
        move(attimeB,b,floirlocantion[1][2])
    # print(f'A계단 시간은..{attimeA}')
    # print(f'B계단 시간은..{attimeB}')
    for timea in range(99,-1,-1):
        if attimeA[timea]==0:
            continue
        else :
            # print("aaaaaaaaaaa",timea)
            floirtime=timea+1
            break
    for timeb in range(99,-1,-1):
        if attimeB[timeb]==0:
            continue
        else :
            if (timeb+1)>floirtime:
                floirtime=timeb+1
    return  floirtime

def move(array,idx,time):
    # print(f'idx : {idx} time : {time}')
    
    for i in range(1,time+1):
        if(array[idx+(time-i)]>=3):
            move(array,idx+time-i+1,time)
            return
    for j in range(idx,idx+time):
        array[j]+=1
    # print("어레이",array)
    return
# print("casesize는",casesize)
for i in range(casesize):
    mincase=10000
    inputcase()
    # print(f'사람수는 {howmanypeople}')
    # print(f'mapsize : ',mapsize)
    # mincase=solve('111111')
    for j in range(2**howmanypeople):  #**howmanypeople
        howcase=bin(j)[2:]
        tmpresult=solve()
        # print(j,"시행 ",tmpresult)
        if(mincase>tmpresult):
            mincase=tmpresult
    print(f'#{i+1} {mincase}')