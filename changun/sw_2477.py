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
    for i in range(caseinfo[0]):
        recept.append(desk(Recepttime[i]))
    for i in range(caseinfo[1]):
        repair.append(desk(Repairtime[i]))
        #고객이 시간이 되면 하나씩 빼준다. 빼줄고객이 없고,작업중이 고객이 없을경우 멈춤.

    for i in range(500):
        for onerecept in recept:
            if onerecept.customer != None:
                flag=1
                break
            flag=-1
        for onerepair in repair:
            if onerepair.customer != None:
                flag=1
                break
            flag=-1
        print(i,flag,CTarrivetime,sep="-----------")
        if flag==-1 and not CTarrivetime:
            break
        idx=0
        while(True):
            if CTarrivetime[idx]==i:
                CTarrivetime.pop(0)
                waitForRecept.append(customer(cn))
                cn+=1
            else :
                break
        for recptdesk in recept:
            if recptdesk.WTnow !=0:
                recptdesk.WTnow -=1
                if recptdesk.WTnow ==0:
                    tmpCustomer = customer(recptdesk.customer.customerNumber)
                    waitForRepair.append(tmpCustomer)
                    recptdesk.customer=None
                    flag=-1
        for repairdesk in repair:
            if repairdesk.WTnow !=0:
                repairdesk.WTnow -=1
                if repairdesk.WTnow ==0:
                    if repairdesk.customer.recept == caseinfo[3] and repairdesk.customer.repair==caseinfo[4]:
                        result+=repairdesk.customer.customerNumber
                    repairdesk.customer=None
        if waitForRecept:
            for recptdesk in range(len(recept)):
                if recept[recptdesk].WTnow==0:
                    recept[recptdesk].WTnow=recept[recptdesk].mytime
                    tmpCT=waitForRecept.pop(0)
                    tmpCT.recept=recptdesk+1
                    recept[recptdesk].customer=tmpCT
        if waitForRepair:
            for repairdesk in range(len(repair)):
                if repair[repairdesk].WTnow==0:
                    repair[repairdesk].WTnow=recept[repairdesk].mytime
                    tmpCT=waitForRepair.pop(0)
                    tmpCT.repair=repairdesk+1
                    repair[repairdesk].customer=tmpCT
    print(result)