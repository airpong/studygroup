for T in range(int(input())):
    N,M,K,a,b=list(map(int,input().split()))
    rcl=list(map(int,input().split()))
    rpl=list(map(int,input().split()))
    tl=list(zip([k+1 for k in range(K)],list(map(int,input().split()))))
    rcinputl=[[0,0] for i in range(N)]
    rpinputl=[[0,0,0] for j in range(M)]
    rcwaiting=[]
    rpwaiting=[]
    ending=[]
    t=0
    while len(ending)<K:
        # 첫 대기열에 넣기
        for get_in in tl:
            if get_in[1]==t:
                rcwaiting.append([get_in[0]])
        # 접수창구에 사람 체크, 없으면 넣기
        for rccheck in range(len(rcl)):
            if rcinputl[rccheck][0]!=0:
                if rcinputl[rccheck][1]+rcl[rccheck]==t:
                    rpwaiting.append([t,rcinputl[rccheck][0],rccheck+1])
                    rcinputl[rccheck]=[0,0]
            if rcwaiting:
                if rcinputl[rccheck][0]==0:
                    rcinputl[rccheck][0]=rcwaiting[0]
                    rcinputl[rccheck][1]=t
                    del rcwaiting[0]
        print(rpwaiting)
        for rpcheck in range(len(rpl)):
            if rpinputl[rpcheck][0]!=0:
                if rpinputl[rpcheck][2]+rpl[rpcheck]==t:
                    ending.append([rpinputl[rpcheck][0][0],rpinputl[rpcheck][1],rpcheck+1])
                    rpinputl[rpcheck]=[0,0,0]
            if rpwaiting:
                if rpinputl[rpcheck][0]==0:
                    rpinputl[rpcheck][0]=rpwaiting[0][1]
                    rpinputl[rpcheck][1]=rpwaiting[0][2]
                    rpinputl[rpcheck][2]=t
                    del rpwaiting[0]
        t+=1
    print(ending)
    summary=0
    for last in range(len(ending)):
        if ending[last][1]==a and ending[last][2]==b:
            summary+=ending[last][0]
    if summary==0:
        summary=-1
    print(f'#{T+1} {summary}')