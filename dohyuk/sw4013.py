def turn(dct,mag) :
    if dct == 1 :
        # 0 0 1 0 0 1 0 0
        # 0 0 0 1 0 0 1 0
        # pop 마지막 insert 처음으로
        mag.insert(0,mag.pop(7))
    elif dct == -1:
        #반대로
        mag.insert(7,mag.pop(0))
    return mag
def turnall(mag,dct,allmag) :
    le_mag = ri_mag = mag #
    le_dct = ri_dct = dct # 반복을 돌기위해 자석위치 값을 저장
    turn_list = [(mag,dct)] #처음 들어오는 자석위치,방향을 턴리스트에 저장
    while le_mag > 0 : #왼쪽을 체크하기 위한 반복
        if allmag[le_mag][6] != allmag[le_mag-1][2] : #왼쪽 자석과 닿은 부분이 다르면
            le_mag -= 1 #자석위치 변경 방향변경
            le_dct *= -1
            turn_list.append((le_mag,le_dct)) #턴리스트 저장
        else :
            break
    while ri_mag < 3 :
        if allmag[ri_mag][2] != allmag[ri_mag+1][6] :
            ri_mag += 1
            ri_dct *= -1
            turn_list.append((ri_mag,ri_dct))
        else :
            break
    for mag,dct in turn_list :
        turn(dct,allmag[mag]) # 필요한부분 다 턴
    return allmag

for a in range(int(input())) : #총 테스트 케이스의 개수 T
    n = int(input()) #회전 횟수
    s = [list(map(int,input().split())) for i in range(4)] #톱니바퀴 정보저장
    info_turn = [list(map(int,input().split())) for i in range(n)] #회전정보저장
    for mag, dct in info_turn :
        s = turnall(mag-1,dct,s)#-1 은 인덱싱을 위한 -1
    result = 0 
    for index,c in enumerate(s) :
        if c[0] == 1 :
            result += 2**index # 점수
    print(f'#{a+1} {result}')