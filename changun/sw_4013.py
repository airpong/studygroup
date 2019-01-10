def solve():
    howmany = int(input())      #톱니바퀴 회전 횟수
    top =[[2,2,2,2,2,2,2,2]]     #톱니바퀴 자성을 저장할 리스트, 원소로 각 톱니바퀴의 자성순서 리스트를 받게된다
    for i in range(4):
        line = list(map(int,input().split()))
        top.append(line)
    top.append([2,2,2,2,2,2,2,2])
    for i in range(howmany):
        how = list(map(int,input().split()))     #톱니바퀴,방향 저장된 리스트
        top[how[0]]=move(top,how[0],how[1],1,1)
    return top

def move(top,idx,direction,lre,rre):   #회전 방향과 리스트가 입력되면 회전된 리스트를 반환해주는 함수
    if idx == 0 or idx == 5:
        return top[idx]
    else :
        left=top[idx][6]
        right=top[idx][2]
        if (top[idx-1][2]-left != 0) and lre==1:
            top[idx-1]=move(top,idx-1,-direction,1,0)
        if (top[idx+1][6]-right != 0) and rre==1:
            top[idx+1]=move(top,idx+1,-direction,0,1)
        if direction == 1:      #시계방향 회전
            tmp=top[idx][-1]
            for i in range(7,0,-1):
                top[idx][i]=top[idx][i-1]
            top[idx][0]=tmp
        elif direction == -1 :      #반시계 방향 회전
            tmp=top[idx][0]
            for i in range(0,7):
                top[idx][i]=top[idx][i+1]
            top[idx][-1]=tmp
    return top[idx]

casesize = int(input())
for i in range(casesize):
    result =0
    val=1
    tops=solve()
    for top in range(1,5):
        result+=tops[top][0]*val
        val=val*2
    print(f'#{i+1} {result}')