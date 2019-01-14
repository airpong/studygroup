def charge(userA,userB,bclist):
    global result
    
def check(user,bclist):
    # print(abs(bclist[0]-user[0])+abs(bclist[1]-user[1]),bclist[2],"진짜 안된단 말야?")
    if abs(bclist[0]-user[0])+abs(bclist[1]-user[1]) <= bclist[2]:
        return True

casesize = int(input())
for i in range(casesize):
    result = 0
    caseinfo=list(map(int,input().split()))
    userA = list(map(int,input().split()))
    userB = list(map(int,input().split()))
    bclist = [list(map(int,input().split())) for i in range(caseinfo[1])]
    Alocation = [1,1]
    Blocation = [10,10]
    charge(Alocation,Blocation,bclist)
    for i in range(caseinfo[0]):
        print(i+1)
        # print(userA[i],userB[i])
        if userA[i]==1:
            # print("1실행")
            Alocation[1]=Alocation[1]-1
        elif userA[i]==2:
            # print("2실행")
            Alocation[0]=Alocation[0]+1
        elif userA[i]==3:
            # print("3실행")
            Alocation[1]=Alocation[1]+1
        elif userA[i]==4:
            # print("4실행")
            Alocation[0]=Alocation[0]-1
        else :
            print("뭔가잘못됨")

        if userB[i]==1:
            Blocation[1]=Blocation[1]-1
        elif userB[i]==2:
            Blocation[0]=Blocation[0]+1
        elif userB[i]==3:
            Blocation[1]=Blocation[1]+1
        elif userB[i]==4:
            Blocation[0]=Blocation[0]-1
        else : 
            print("뭔가 잘못된줄 알았음 ㅎㅎ")
        charge(Alocation,Blocation,bclist)
    print(result)