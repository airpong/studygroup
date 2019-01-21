def search(item,loof) :
    t1 = item
    i = loof
    result = 0
    for k in range(i,0,-1) :
        temp = t1//10**k
        for p in range(1,temp) :
            result += p*10**k
        result += temp*(t1%10**k+1)
        #print(result)
        result += k*(t1//10**k) * (10**(k-1))*45
        #print(k,k*t1//10**k * 10**(k-1)*45)
        t1 = t1%10**k
    result += (t1*(t1+1))//2
    return result
for a in range(int(input())) :
    b,c = list(map(int,input().split()))
    i = j = 0
    t1 = b
    t2 = c
    l1 = []
    l2 = []
    while True :
        if t1 < 10 and t2 < 10 :
            break
        if t1 > 9 :
            t1 //= 10
            i += 1
        if t2 > 9 :
            t2 //= 10
            j += 1
    #sprint(search(b,i))
    if b == 0 :
        b=1
    print(f'#{a+1} {search(c,j)-search(b-1,i)}')
    #최대 자리에 대한 그다음자리 
    #b//10**i * 10**(i-1)
    # t1 = b
    # result = 0
    # for k in range(i,0,-1) :
    #     temp = t1//10**k
    #     for p in range(1,temp) :
    #         result += p*10**k
    #     result += temp*(t1%10**k+1)
    #     print(result)
    #     result += k*t1//10**k * 10**(k-1)*45
    #     print(k,k*t1//10**k * 10**(k-1)*45)
    #     t1 = t1%10**k
    # result += (t1*(t1+1))//2
    # print(result)
        
