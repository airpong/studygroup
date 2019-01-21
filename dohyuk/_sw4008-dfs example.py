def dfs(time,result,pre_operand) :

    global num
    global my_max
    global my_min
    global pos

    if time >= len(num) :
        my_max = max(my_max,result)
        my_min = min(my_min,result)
        return
    pos +=1 
    my_operand = list(pre_operand)
   # print(pos,my_operand,time,result)
    for i in range(len(my_operand)) :
        if my_operand[i] > 0:
            my_operand[i] -= 1
            if i == 0 :
                result += num[time]
                result1 = result + num[time]
            elif i == 1:
                #my_operand[i] -= 1
                result1 = result - num[time]
            elif i == 2:
                #my_operand[i] -= 1
                result1 = result * num[time]
            elif i == 3:
               # my_operand[i] -= 1
                result1 = int(result/num[time])
            dfs(time+1,result1,my_operand)
            my_operand[i] += 1
           


for a in range(int(input())) : #총 테스트 케이스의 개수 T
    n= int(input())
    pre_operand = list(map(int,input().split()))
    num = list(map(int,input().split()))
    my_max = -9999
    my_min = 9999 
    #result = 0
    pos = 0
    dfs(1,num[0],pre_operand)
    print(my_max,my_min)
    print(f'#{a+1} {my_max-my_min}')