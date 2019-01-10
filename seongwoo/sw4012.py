for i in range(int(input())):
    n=int(input())
    a=[list(map(int,input().split())) for i in range(n)]
    indexa=[] # A요리 재료 인덱스
    indexb=[] # B요리 재료 인덱스
    # 토큰에 바이너리로 1,0 구분해서 A,B 요리재료 인덱스 나눠 넣음
    for j in range(2**(n-1),2**n):
        token=bin(j)[2:]
        b=[]
        c=[]
        if token.count('1')==n//2:
            for k in range(len(token)):
                if token[k]=='1':
                    b.append(k)
                else:
                    c.append(k)
        if b:
            indexa.append(b)
        if c:
            indexb.append(c)
    scores=[] #스코어 차이 싹 다 넣을 곳
    # A,B 재료 페어 당 시너지 합계 각각 저장해서 점수 냄
    for o in range(len(indexa)):
        ascore=0
        bscore=0
        z=indexa[o]
        y=indexb[o]
        for m in range(n//2):
            for w in range(m+1,n//2):
                ascore+=(a[z[m]][z[w]]+a[z[w]][z[m]])
                bscore+=(a[y[m]][y[w]]+a[y[w]][y[m]])
        scores.append(abs(ascore-bscore))
    print(f'#{i+1} {min(scores)}')