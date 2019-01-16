def opena(col,row,pos,width,height):
    # print("mycolandrow",col,row)
    global tools
    global result
    mytool=tools[col][row]
    if pos<=1:
        result.append((col,row))
        return
    elif mytool==0:
        return
    else:
        result.append((col,row))
        tools[col][row]=0
        if mytool==1:
            if row>0:       #왼쪽으로 보내기
                if tools[col][row-1]==3 or tools[col][row-1]==4 or tools[col][row-1]==5 or tools[col][row-1]==1:
                    opena(col,row-1,pos-1,width,height)
                    tools[col][row]=mytool
            if row<width-1:     #오른쪽으로 보내기
                if tools[col][row+1]==3 or tools[col][row+1]==1 or tools[col][row+1]==6 or tools[col][row+1]==7:
                    opena(col,row+1,pos-1,width,height)
                    tools[col][row]=mytool
            if col>0:       #위로 보내기
                if tools[col-1][row]==1 or tools[col-1][row]==2 or tools[col-1][row]==5 or tools[col-1][row]==6:
                    opena(col-1,row,pos-1,width,height)
                    tools[col][row]=mytool
            if col<height-1:    #아래로 보내기
                if tools[col+1][row]==1 or tools[col+1][row]==2 or tools[col+1][row]==4 or tools[col+1][row]==7:
                    opena(col+1,row,pos-1,width,height)
                    tools[col][row]=mytool
        if mytool==2:
            if col>0:       #위로 보내기
                if tools[col-1][row]==1 or tools[col-1][row]==2 or tools[col-1][row]==5 or tools[col-1][row]==6:
                    opena(col-1,row,pos-1,width,height)
                    tools[col][row]=mytool
            if col<height-1:    #아래로 보내기
                if tools[col+1][row]==1 or tools[col+1][row]==2 or tools[col+1][row]==4 or tools[col+1][row]==7:
                    opena(col+1,row,pos-1,width,height)
                    tools[col][row]=mytool
        if mytool==3:
            if row>0:       #왼쪽으로 보내기
                if tools[col][row-1]==3 or tools[col][row-1]==4 or tools[col][row-1]==5 or tools[col][row-1]==1:
                    opena(col,row-1,pos-1,width,height)
                    tools[col][row]=mytool
            if row<width-1:     #오른쪽으로 보내기
                if tools[col][row+1]==3 or tools[col][row+1]==1 or tools[col][row+1]==6 or tools[col][row+1]==7:
                    opena(col,row+1,pos-1,width,height)
                    tools[col][row]=mytool
        if mytool==4:
            if col>0:       #위로 보내기
                if tools[col-1][row]==1 or tools[col-1][row]==2 or tools[col-1][row]==5 or tools[col-1][row]==6:
                    opena(col-1,row,pos-1,width,height)
                    tools[col][row]=mytool
            if row<width-1:     #오른쪽으로 보내기
                if tools[col][row+1]==3 or tools[col][row+1]==1 or tools[col][row+1]==6 or tools[col][row+1]==7:
                    opena(col,row+1,pos-1,width,height)
                    tools[col][row]=mytool
        if mytool==5:
            if row<width-1:     #오른쪽으로 보내기
                if tools[col][row+1]==3 or tools[col][row+1]==1 or tools[col][row+1]==6 or tools[col][row+1]==7:
                    opena(col,row+1,pos-1,width,height)
                    tools[col][row]=mytool
            if col<height-1:    #아래로 보내기
                if tools[col+1][row]==1 or tools[col+1][row]==2 or tools[col+1][row]==4 or tools[col+1][row]==7:
                    opena(col+1,row,pos-1,width,height)
                    tools[col][row]=mytool
        if mytool==6:
            if col<height-1:    #아래로 보내기
                if tools[col+1][row]==1 or tools[col+1][row]==2 or tools[col+1][row]==4 or tools[col+1][row]==7:
                    opena(col+1,row,pos-1,width,height)
                    tools[col][row]=mytool
            if row>0:       #왼쪽으로 보내기
                if tools[col][row-1]==3 or tools[col][row-1]==4 or tools[col][row-1]==5 or tools[col][row-1]==1:
                    opena(col,row-1,pos-1,width,height)
                    tools[col][row]=mytool
        if mytool==7:
            if row>0:       #왼쪽으로 보내기
                if tools[col][row-1]==3 or tools[col][row-1]==4 or tools[col][row-1]==5 or tools[col][row-1]==1:
                    opena(col,row-1,pos-1,width,height)
                    tools[col][row]=mytool
            if col>0:       #위로 보내기
                if tools[col-1][row]==1 or tools[col-1][row]==2 or tools[col-1][row]==5 or tools[col-1][row]==6:
                    opena(col-1,row,pos-1,width,height)
                    tools[col][row]=mytool

                    
casesize=int(input())
for i in range(casesize):
    result=[]
    caseinfo = list(map(int,input().split()))
    tools=[list(map(int,input().split())) for i in range(caseinfo[0])]
    opena(caseinfo[2],caseinfo[3],caseinfo[4],caseinfo[1],caseinfo[0])
    print(f'#{i+1} {len(set(result))}')
