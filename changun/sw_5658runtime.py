case_size = int(input())
for i in range(case_size):
    info = list(map(int,input().split()))
    number = input()
    intlst = []
    for j in range(3):
        if j != 0:
            number=number[-1]+number[:-1]
        else :
            pass
        lst = [number[j:j+int(info[0]/4)] for j in range(0,info[0],int(info[0]/4))]
        for j in lst:
            intlst.append(int(j,16))
    intlst=list(set(intlst))
    intlst.sort()
    print(f'#{i+1} {intlst[len(intlst)-info[1]]}')
