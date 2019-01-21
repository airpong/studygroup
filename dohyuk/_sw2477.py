for c in range(int(input())) :
    n,m,k,a,b = list(map(int,input().split()))
    timea = list(map(int,input().split()))
    timeb = list(map(int,input().split()))
    timek = list(map(int,input().split()))
    timekc = timek[:]
    quea = []
    queb = []
    queka = []
    quekb = []
    for t in timea:
        temp = [0 for i in range(t)]
        quea.append(temp)
    for t in timeb:
        temp = [0 for i in range(t)]
        queb.append(temp)
    time = 0
    number = 1
    result1 = []
    result2 = []
    stop = 1
    while stop :
        if min(timek) > time :
            time+=1
            continue
        stop = 0
        for t in timek :
            if t == time :
                queka.append(number)
                timekc.pop(0)
                number+=1
        for q in quea:
            item = q.pop(0)
            if item :
                quekb.append(item)
        for q in queb:
            q.pop(0)
        for idx,t in enumerate(quea) :
            check = False
            for p in t :
                if p :
                    check = True
                    break
            if check == False :
                if queka :
                    item = queka.pop(0)
                    t.append(item)
                    # print(item,idx,a-1)
                    if idx == a-1 :
                        result1.append(item)
                    continue
            t.append(0)
        for idx,t in enumerate(queb) :
            check = False
            for p in t :
                if p :
                    check = True
                    break
            if check == False :
                if quekb :
                    item = quekb.pop(0)
                    t.append(item)
                    #print(item,idx,b-1)
                    if idx == b-1 :
                        result2.append(item)
                    continue
            t.append(0)
        time += 1
        for p in quea :
            for t in p :
                if t :
                    stop = 1
                    break
        for p in queb :
            for t in p :
                if t :
                    stop = 1
                    break
        for p in queka :
            if p :
                stop = 1
                break
        for p in quekb :
            if p :
                stop = 1
                break
        for p in timekc :
            if p :
                stop = 1
                break
        # if max(timek) < time :
        #     print(max(timek))
        #     stop = 0
    result = 0
    print(time)
    print(result1)
    print(result2)
    for i in result1:
        if i in result2 :
            result += i
    print(f'#{c+1} {result if result else -1}')