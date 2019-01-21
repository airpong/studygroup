class desk():
    def __init__(self, time):
        self.mytime = time
        self.WTnow = 0
        self.customer = None
class customer():
    def __init__(self,n):
        self.customerNumber=n
        self.recept=0
        self.repair=0

casesize=int(input())
for case in range(casesize):
    caseinfo=list(map(int,input().split()))
    Recepttime = list(map(int,input().split()))
    Repairtime = list(map(int,input().split()))
    CTarrivetime = list(map(int,input().split()))
    cn=1
    waitForRecept = []
    waitForRepair = []
    recept = []
    repair = []
    result = 0
    aflag = -1
    bflag = -1
    for i in range(caseinfo[0]):
        recept.append(desk(Recepttime[i]))
    for i in range(caseinfo[1]):
        repair.append(desk(Repairtime[i]))
        #고객이 시간이 되면 하나씩 빼준다. 빼줄고객이 없고,작업중이 고객이 없을경우 멈춤.
    for i in range(1100):
        # print()
        for onerecept in recept:
            if onerecept.customer!=None:
                # print("접수처에 누가있음?")
                aflag=1
                break
            aflag=-1
        for onerepair in repair:
            if onerepair.customer != None:
                # print("으아니?")
                bflag=1
                break
            bflag=-1
        # print(i,aflag,bflag,CTarrivetime,"빼기전",sep="****")
        if bflag==-1 and aflag==-1 and len(CTarrivetime)==0:
            # print("이거 끝남")
            break
        idx=0
        while(True):
            if not CTarrivetime:
                break
            elif CTarrivetime[idx]==i:
                # print(CTarrivetime.pop(0),"빠짐 고객번호 : ",cn)
                CTarrivetime.pop(0)
                waitForRecept.append(customer(cn))
                # print("접수를 위해 기다리는 사람",len(waitForRecept))
                cn+=1
            else :
                break
        for recptdesk in recept:
            if recptdesk.WTnow !=0:
                # print("이번시간이 지나고 접수처에 고객이 누군가는 있음")
                recptdesk.WTnow -=1
                # print("접수처 남은시간",recptdesk.WTnow)
                if recptdesk.WTnow ==0:
                    # print("이번시간이 지나고 접수처에 고객이 아무도 없음")
                    tmpCustomer = customer(recptdesk.customer.customerNumber)
                    tmpCustomer.recept=recptdesk.customer.recept
                    waitForRepair.append(tmpCustomer)
                    # print("몇명대기하고 있냐면 리페어를 위해",len(waitForRepair))
                    recptdesk.customer=None
                    flag=-1
        for repairdesk in repair:
            if repairdesk.WTnow !=0:
                # print("수리처에 고객이 누군가는 있음")
                repairdesk.WTnow -=1
                # print("수리처 남은시간",repairdesk.WTnow)
                if repairdesk.WTnow ==0:
                    # print("접수처에 고객이 아무도 없음")
                    # print("어디서 접수하고 어디서 수리받았나",repairdesk.customer.recept,repairdesk.customer.repair)
                    if repairdesk.customer.recept == caseinfo[3] and repairdesk.customer.repair==caseinfo[4]:
                        # print("원하던사람 찾음")
                        result+=repairdesk.customer.customerNumber
                        # print("현재 리절트",result)
                    repairdesk.customer=None
        if waitForRecept:
            # print("누군가 접수를 위해 대기중")
            for recptdesk in range(len(recept)):
                if recept[recptdesk].WTnow==0:
                    # print("비어있는 접수처 있음")
                    recept[recptdesk].WTnow=recept[recptdesk].mytime
                    tmpCT=waitForRecept.pop(0)
                    tmpCT.recept=recptdesk+1
                    recept[recptdesk].customer=tmpCT
                    if not waitForRecept:
                        break
        if waitForRepair:
            # print("누군가 수리를 위해 대기중")
            for repairdesk in range(len(repair)):
                if repair[repairdesk].WTnow==0:
                    # print("비어있는 수리처 있음")
                    repair[repairdesk].WTnow=repair[repairdesk].mytime
                    tmpCT=waitForRepair.pop(0)
                    tmpCT.repair=repairdesk+1
                    repair[repairdesk].customer=tmpCT
                    if not waitForRepair:
                        break
    if result == 0:
        result=-1
    print(f'#{case+1} {result}')