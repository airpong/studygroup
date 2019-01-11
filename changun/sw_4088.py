def DFS(pos,result):
    global number
    global oper
    global result_max
    global result_min
    if pos>=len(number):
        if result>result_max:
            result_max=result
        if result<result_min:
            result_min=result
        return
    else :
        for i in range(4):
            tmpresult=result
            if oper[i]>0:
                if i==0 :
                    tmpresult=result+number[pos]
                elif i==1 :
                    tmpresult=result-number[pos]
                elif i==2 :
                    tmpresult = result*number[pos]
                elif i==3 :
                    tmpresult = int(result/number[pos])
                else :
                    print("오퍼레이션 인덱션 잘못됨")
                oper[i]=oper[i]-1
                DFS(pos+1,tmpresult)
                oper[i]=oper[i]+1

casesize = int(input())
for i in range(casesize):
    count_number = int(input())
    oper = list(map(int,input().split()))
    number = list(map(int,input().split()))
    result=number[0]
    result_max=-1000000
    result_min=1000000
    DFS(1,result)
    print(f'#{i+1} {result_max-result_min}')