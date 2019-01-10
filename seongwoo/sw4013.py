def list_circle(x,y):
    if x==-1:
        temp=y[0]
        for i in range(1,8):
            y[i-1]=y[i]
        y[7]=temp
    if x==1:
        temp=y[7]
        for i in range(7,0,-1):
            y[i]=y[i-1]
        y[0]=temp

for i in range(int(input())): # t 동안
    k=int(input()) # k번
    m=[]
    for j in range(4):
        m.append(list(map(int,input().split())))
    for o in range(k):
        how=[[m[0][2],m[1][6]],[m[1][2],m[2][6]],[m[2][2],m[3][6]]] # 자석 붙어있는 극 번호
        check=[0,0,0,0] # 자석 당 회전 여부 및 방향
        num,rotation=list(map(int,input().split())) # 회전할 자석, 방향
        check[num-1]=rotation
        for left in range(num-2,-1,-1): # 돌리는 자석 왼쪽으로 쭉 확인
            if num>1:
                if how[left][0]!=how[left][1]:
                    check[left]=check[left+1]*-1
        for right in range(num-1,3): # 돌리는 자석 오른쪽으로 쭉 확인
            if num<4:
                if how[right][0]!=how[right][1]:
                    check[right+1]=check[right]*-1
        for x in range(len(check)): # check 값 확인하고 알맞게 회전
            list_circle(check[x],m[x])
    print(f'#{i+1} {m[0][0]+m[1][0]*2+m[2][0]*4+m[3][0]*8}')