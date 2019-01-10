from itertools import combinations 
def solve():
    NumOfFood = int(input())
    foods = []
    resultMax = 100000
    SumOfAll =0
    for i in range(NumOfFood):
        foods.append(list(map(int,input().split())))
    for i in foods:
        SumOfAll+=sum(i)
    for i in combinations(range(NumOfFood),NumOfFood//2):
        SelectedSum=0
        UnSelected=0
        tmpfoods = list(range(NumOfFood))
        for j in i:
            tmpfoods.remove(j)
        for col in i:
            for row in i:
                if col==row:
                    continue
                else :
                    SelectedSum+=foods[col][row]
        for col in tmpfoods:
            for row in tmpfoods:
                if col==row:
                    continue
                else :
                    UnSelected+=foods[col][row]        
        if(abs(SelectedSum-UnSelected)<resultMax):
            resultMax=abs(SelectedSum-UnSelected)
    return resultMax


casesize = int(input())
for i in range(casesize):
    result = solve()
    print(f'#{i+1} {result}')
