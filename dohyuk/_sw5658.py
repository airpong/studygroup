for a in range(int(input())) :
    n,k= list(map(int,input().split()))
    item = input()
    lt = []
    chknum = n//4
    for j in range(chknum) :
        for i in range(4) :
            lt.append(item[i*chknum:(i+1)*chknum])
        item = list(item)
        temp = item.pop()
        item.insert(0,temp)
        item = ''.join(item)
    re = []
    print(lt)
    for i in lt:
        te = '0x'+i
        re.append(int(te,16))
    re = sorted(list(set(re)),reverse=True)
    print(re)
    print(f'#{a+1} {re[k-1]}')
        

    