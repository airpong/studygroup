def dfs(t,re) :
    global my_min,bill,useage
    if t >= 13 :
        if re < my_min :
            my_min = re
        return
    dfs(t+1,re+useage[t-1]*bill[0])
    dfs(t+1,re+bill[1])
    dfs(t+3,re+bill[2])
    dfs(t+12,re+bill[3])
    
    
for a in range(int(input())) : #총 테스트 케이스의 개수 T
    bill = list(map(int,input().split()))
    useage = list(map(int,input().split()))
    my_min = bill[3]
    dfs(1,0)
    print(f'#{a+1} {my_min}')
    #testst