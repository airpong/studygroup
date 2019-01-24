for T in range(int(input())):
    n,m,k=list(map(int,input().split()))
    crowds=[]
    for i in range(k):
        # 세로 가로 수 방향
        # 상 하 좌 우 1 2 3 4
        crowds.append(list(map(int,input().split())))
    for time in range(1,m+1):
        time_pos={}
        delist=[]
        for i in range(len(crowds)):
            crowd=crowds[i]
            # 일단 이동
            to=crowd[3]
            if to==1:
                crowd[0]-=1
            if to==2:
                crowd[0]+=1
            if to==3:
                crowd[1]-=1
            if to==4:
                crowd[1]+=1
            # 이동한 곳에 누가 있나 확인
            if time_pos.get((crowd[0],crowd[1]))==None:
                # 없으니 내가 드감
                time_pos[(crowd[0],crowd[1])]=[crowd[2],i,crowd[2]]
            else:
                # 있으면 값 비교하고 지워질 놈 인덱스 저장해둠
                nowpos=time_pos[(crowd[0],crowd[1])]
                nowpos[0]+=crowd[2]
                if crowd[2]>nowpos[2]:
                    temp,nowpos[1]=nowpos[1],i
                    nowpos[2]=crowd[2]
                    crowd[2]=nowpos[0]
                    delist.append(temp)
                else:
                    delist.append(i)
                    crowds[nowpos[1]][2]=nowpos[0]
            # 제일 바깥쪽 가면 일단 방향 체인지
            if crowd[0]==0 or crowd[0]==n-1 or crowd[1]==0 or crowd[1]==n-1:
                if to==1:
                    crowd[3]=2
                if to==2:
                    crowd[3]=1
                if to==3:
                    crowd[3]=4
                if to==4:
                    crowd[3]=3
                # 반 죽음
                crowd[2]//=2
        # 지워질 놈은 지움
        delist.sort()
        token=0
        for i in delist:
            del crowds[i-token]
            token+=1
    summary=0
    for crowd in crowds:
        summary+=crowd[2]
    print(f'#{T+1} {summary}')