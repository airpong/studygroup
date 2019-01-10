def searchmin(sbinary,allmap) :
    foodA = []
    foodB = [] # 음식에 들어갈 식재료 번호를 저장할 리스트
    for i in range(len(sbinary)):
        if sbinary[i] == '1' : #binary숫자가 1일때 foodA
            foodA.append(i)
        else :
            foodB.append(i)
    resultA = resultB = 0 #A,B의 합산점수
    for i in foodA :
        for j in foodA :
            if i == j : #i,j가 같으면 무시
                continue
            resultA+=allmap[i][j] #아니면 점수를 더해준다
    for i in foodB :
        for j in foodB :
            if i == j :
                continue
            resultB+=allmap[i][j]
    return abs(resultA-resultB)


for a in range(int(input())) : #총 테스트 케이스의 개수 T
    n = int(input()) #테스트케이스 n*n
    s = [list(map(int,input().split())) for i in range(n)] #행렬 생성
    t = 2**n # t binary를 위한 변수
    m = k = 160001 # 시너지의 최대값 20000 * 갯수 8
    for i in range(t//2,t) : #바이너리 검색
        sbinary = bin(i)[2:].zfill(n)
        if sbinary.count('1') == n//2 : # 반으로 정확히 나눠진경우
        #-- 최소값
            k = searchmin(sbinary,s)
            if m > k :
                m = k
        #-- 최소값
    print(f'#{a+1} {m}')
