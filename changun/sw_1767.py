class core():       #core 클래스 해당 코어와 연결가능한 가지의 리스트 속성을 가지고있음
    def __init__(self,x,y):
        self.col=x
        self.row=y
        self.linkedLine=[]

class line():       #선 클래스/코어의 위치, 길이, 내 번호, 연결 불가능한 가지의 리스트
    count=0
    def __init__(self,x,y,direct,LEN):
        self.mydirection=direct
        self.mynum=line.count
        self.col=x
        self.row=y
        self.distance=LEN
        self.linkedOther = []
        line.count+=1

def solve(cores,lst,pos,corenum,alldistance):
    global Maxcore
    global Mindistance
    if pos>=len(cores):
        if corenum>Maxcore:
            Maxcore=corenum
            Mindistance=alldistance
            # if alldistance<Mindistance:
        elif corenum==Maxcore:
            if alldistance<Mindistance:
                Mindistance=alldistance
        return
    # print("a",pos,len(cores[pos].linkedLine))
    for line in range(len(cores[pos].linkedLine)+1):      #+1넣어라
        # print(pos,line)
        if line == len(cores[pos].linkedLine):
            solve(cores,lst,pos+1,corenum,alldistance)
        else:
            flag = 0
            for noise in cores[pos].linkedLine[line].linkedOther:
                if noise in lst:
                    flag=1
                    break
            if flag==1:

                continue
            else:
                lst.append(cores[pos].linkedLine[line].mynum)
                corenum+=1
                alldistance+=cores[pos].linkedLine[line].distance
                # if lst[0]==0:
                #     print(lst,corenum,alldistance)
                solve(cores,lst,pos+1,corenum,alldistance)
                corenum-=1
                alldistance-=cores[pos].linkedLine[line].distance
                lst.pop()
def link(coreList,lineList):
    for core in coreList:
        for i in range(0,core.col+1):
            if i==core.col:
                tmp=line(core.col,core.row,0,i)
                core.linkedLine.append(tmp)
                lineList.append(tmp)
            elif caseArr[i][core.row]==0:
                continue
            else:
                break
        for i in range(core.col+1,N+1):
            if i==N:
                tmp=line(core.col,core.row,2,N-core.col-1)
                core.linkedLine.append(tmp)
                lineList.append(tmp)
            elif caseArr[i][core.row]==0:
                continue
            else:
                break
        for i in range(0,core.row+1):
            if i==core.row:
                tmp=line(core.col,core.row,3,i)
                core.linkedLine.append(tmp)
                lineList.append(tmp)
            elif caseArr[core.col][i]==0:
                continue
            else:
                break
        for i in range(core.row+1,N+1):
            if i==N:
                tmp=line(core.col,core.row,1,N-core.row-1)
                core.linkedLine.append(tmp)
                lineList.append(tmp)
            elif caseArr[core.col][i]==0:
                continue
            else:
                break

def checkline(lineList):
    for line in lineList:
         for checkline in lineList:
            if line.mynum==checkline.mynum:
                continue
            else :
                if line.mydirection%2==checkline.mydirection%2:
                    continue
                else:
                    if line.mydirection==0:
                        if checkline.mydirection==1:
                            if checkline.col<line.col:
                                if checkline.row<line.row:
                                    line.linkedOther.append(checkline.mynum)
                        if checkline.mydirection==3:
                            if checkline.col<line.col:
                                if checkline.row>line.row:
                                    line.linkedOther.append(checkline.mynum)
                    if line.mydirection==1:
                        if checkline.mydirection==0:
                            if checkline.row>line.row:
                                if checkline.col>line.col:
                                    line.linkedOther.append(checkline.mynum)
                        if checkline.mydirection==2:
                            if checkline.row>line.row:
                                if checkline.col<line.col:
                                    line.linkedOther.append(checkline.mynum)
                    if line.mydirection==2:
                        if checkline.mydirection==1:
                            if checkline.row<line.row:
                                if checkline.col>line.col:
                                    line.linkedOther.append(checkline.mynum)
                        if checkline.mydirection==3:
                            if checkline.row>line.row:
                                if checkline.col>line.col:
                                    line.linkedOther.append(checkline.mynum)
                    if line.mydirection==3:
                        if checkline.mydirection==0:
                            if checkline.row<line.row:
                                if checkline.col>line.col:
                                    line.linkedOther.append(checkline.mynum)
                        if checkline.mydirection==2:
                            if checkline.row<line.row:
                                if checkline.col<line.col:
                                    line.linkedOther.append(checkline.mynum)


casesize=int(input())
for case in range(casesize):
    Maxcore=0
    Mindistance=100000
    N = int(input())
    caseArr = [list(map(int,input().split())) for i in range(N)]
    coreList=[]
    for col in range(1,N-1):
        for row in range(1,N-1):
            if caseArr[col][row]!=0:
                coreList.append(core(col,row))
    lineList = []
    link(coreList,lineList)
    checkline(lineList)
    # for core in coreList:
    #     print("--",core.col,core.row)
    #     for line in core.linkedLine:
    #         print(line.mynum,line.mydirection,line.linkedOther,line.distance)

    nowlinked=[]
    solve(coreList,nowlinked,0,0,0)
    # for line in lineList:
    #     print("line",line.mynum)
    #     for linked in line.linkedOther:
    #         print(linked)
    print(Maxcore,Mindistance)
