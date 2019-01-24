def solve(startCol,startRow,col,row,array,direction,blackholl):
    count=0
    while(True):
        col,row=move(col,row,direction)
        # print("a`",array[col][row],count)
        if (col,row)==(startCol,startRow):
            break
        if array[col][row]!=0:
            if array[col][row]<=5 and array[col][row]>0:
                count+=1
            col,row,direction=check(col,row,array,direction,blackholl)
            if direction==-1:
                # print(count)
                break
        # print(col,row,direction,count)
    return count

def move(col,row,direction):
    if direction==0:
        return col-1,row
    elif direction==1:
        return col,row+1
    elif direction==2:
        return col+1,row
    elif direction==3:
        return col,row-1
def check(x,y,array,direction,blackholl):
    if array[x][y]==-1:
        return x,y,-1
    elif array[x][y]==1:
        tmp=[2,3,1,0]
        return x,y,tmp[direction]
    elif array[x][y]==2:
        tmp=[1,3,0,2]
        return x,y,tmp[direction]
    elif array[x][y]==3:
        tmp=[3,2,0,1]
        return x,y,tmp[direction]
    elif array[x][y]==4:
        tmp=[2,0,3,1]
        return x,y,tmp[direction]
    elif array[x][y]==5:
        tmp=[2,3,0,1]
        return x,y,tmp[direction]
    elif array[x][y] <=10 and array[x][y]>=0 :
        if (x,y)==blackholl[array[x][y]][0]:
            (x,y)=blackholl[array[x][y]][1]
        else:
            (x,y)=blackholl[array[x][y]][0]
        return x,y,direction
    

casesize = int(input())
for case in range(casesize):
    caseinfo=int(input())
    caseArr=[[5]+list(map(int,input().split()))+[5] for i in range(caseinfo)]
    caseArr.insert(0,[5]*(caseinfo+2))
    caseArr.append([5]*(caseinfo+2))
    blackholl={}
    for col in range(caseinfo+2):
        for row in range(caseinfo+2):
            if caseArr[col][row]>=6 and caseArr[col][row]<=10:
                if not blackholl.get(caseArr[col][row]):
                    blackholl[caseArr[col][row]]=[(col,row)]
                else:
                    blackholl[caseArr[col][row]].append((col,row))
    result=0
    # print(blackholl)
    for locationCol in range(1,caseinfo+1):
        for locationRow in range(1,caseinfo+1):
            if caseArr[locationCol][locationRow]==0:
                for direction in range(4):
                    tmpresult=solve(locationCol,locationRow,locationCol,locationRow,caseArr,direction,blackholl)
                    if tmpresult>result:
                        result=tmpresult
    print(result)