from itertools import permutations
import time
casesize = int(input())
for i in range(casesize):
    numsize = int(input())
    opercount = input().split()
    nums = list(map(int,input().split()))
    start_time = time.time()
    oper = {'+':0,'-':0,'*':0,'/':0}
    operlist = []

    for key,i in zip(oper,range(4)):
        oper[key]=int(opercount[i])
    for operater in oper:
        for i in range(oper[operater]):
            operlist.append(operater)
    Maxofcase = -10000
    Minofcase = 10000
        # 숫자 조합중 하나
    for op in set(permutations(operlist)):   #연산자 조합중 하나
        tmpnum=nums.copy()
        for onething in op:
            if onething == '+':
                tmpnum[0]=tmpnum[0]+tmpnum[1]
                tmpnum.pop(1)
            elif onething == '-':
                tmpnum[0]=tmpnum[0]-tmpnum[1]
                tmpnum.pop(1)
            elif onething == '*':
                tmpnum[0]=tmpnum[0]*tmpnum[1]
                tmpnum.pop(1)
            elif onething == '/':
                tmpnum[0]=int(tmpnum[0]/tmpnum[1])
                tmpnum.pop(1)
        if tmpnum[0]>Maxofcase:
            Maxofcase=tmpnum[0]
        if tmpnum[0]<Minofcase:
            Minofcase=tmpnum[0]
    print(f'#{i+1} {Maxofcase-Minofcase}')
print("--- %s seconds ---" %(time.time() - start_time))