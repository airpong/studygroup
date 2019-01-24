class Ball():
    def __init__(self,x,y,way):
        self.x=x
        self.y=y
        # 상 하 좌 우 0 1 2 3
        self.way=way
        self.now=gameboard[x][y]
 
    def setpos(self,x,y):
        self.now=gameboard[x][y]
for T in range(int(input())):
    n=int(input())
    gameboard=[]
    hole=[]
    score=0
    for i in range(n):
        gameboard.append(list(map(int,input().split())))
        for j in range(n):
            if gameboard[i][j]>5:
                hole.append((gameboard[i][j],i,j))
    for i in range(n):
        for j in range(n):
            if gameboard[i][j]==0:
                for k in range(4):
                    tryscore=0
                    ball=Ball(i,j,k)
                    while 1:
                        if ball.way==0:
                            ball.x-=1
                            # 벽이면
                            if ball.x<0:
                                tryscore+=1
                                ball.now=0
                            else:
                                ball.setpos(ball.x,ball.y)
                            # 블록이면
                            if ball.now in [1,4,5]:
                                ball.way=1
                                tryscore+=1
                            if ball.now==2:
                                ball.way=3
                                tryscore+=1
                            if ball.now==3:
                                ball.way=2
                                tryscore+=1
                            if ball.now>5:
                                for pos in hole:
                                    if pos[0]==ball.now and (pos[1]!=ball.x or pos[2]!=ball.y):
                                        ball.x=pos[1]
                                        ball.y=pos[2]
                                        break
                            if ball.x<0:
                                ball.way=1
                        elif ball.way==1:
                            ball.x+=1
                            if ball.x>n-1:
                                tryscore+=1
                                ball.now=0
                            else:
                                ball.setpos(ball.x,ball.y)
                            if ball.now in [2,3,5]:
                                ball.way=0
                                tryscore+=1
                            if ball.now==1:
                                ball.way=3
                                tryscore+=1
                            if ball.now==4:
                                ball.way=2
                                tryscore+=1
                            if ball.now>5:
                                for pos in hole:
                                    if pos[0]==ball.now and (pos[1]!=ball.x or pos[2]!=ball.y):
                                        ball.x=pos[1]
                                        ball.y=pos[2]
                                        break
                            if ball.x>n-1:
                                ball.way=0
                        elif ball.way==2:
                            ball.y-=1
                            if ball.y<0:
                                tryscore+=1
                                ball.now=0
                            else:
                                ball.setpos(ball.x,ball.y)
                            if ball.now in [3,4,5]:
                                ball.way=3
                                tryscore+=1
                            if ball.now==1:
                                ball.way=0
                                tryscore+=1
                            if ball.now==2:
                                ball.way=1
                                tryscore+=1
                            if ball.now>5:
                                for pos in hole:
                                    if pos[0]==ball.now and (pos[1]!=ball.x or pos[2]!=ball.y):
                                        ball.x=pos[1]
                                        ball.y=pos[2]
                                        break
                            if ball.y<0:
                                ball.way=3
                        elif ball.way==3:
                            ball.y+=1
                            if ball.y>n-1:
                                tryscore+=1
                                ball.now=0
                            else:
                                ball.setpos(ball.x,ball.y)
                            if ball.now in [1,2,5]:
                                ball.way=2
                                tryscore+=1
                            if ball.now==3:
                                ball.way=1
                                tryscore+=1
                            if ball.now==4:
                                ball.way=0
                                tryscore+=1
                            if ball.now>5:
                                for pos in hole:
                                    if pos[0]==ball.now and (pos[1]!=ball.x or pos[2]!=ball.y):
                                        ball.x=pos[1]
                                        ball.y=pos[2]
                                        break
                            if ball.y>n-1:
                                ball.way=2
                        if (ball.x==i and ball.y==j) or ball.now==-1:
                            if tryscore>score:
                                score=tryscore
                            break
    print(f'#{T+1} {score}')