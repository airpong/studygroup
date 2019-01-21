for a in range(int(input())) :
    n,m,k = list(map(int,input().split()))
    item = [list(map(int,input().split())) for i in range(n)]
    allmap = [[0 for i in range(1001)] for i in range(1001)]
    for i in range(n):
        for j in range(m) :
            allmap[499+i][499+j] = item[j][i] * 2
    time = 0
    while time <= k :
        