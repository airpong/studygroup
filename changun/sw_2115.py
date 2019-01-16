def colmax(lst,box,boxsize):
    result=0
    length=2**box
    print(length)
    for i in range(len(lst)-box+1):
        for j in range(length):
            tmpresult=0
            Sumof1=0
            a=str(bin(j))[2:].zfill(box)
            print(a)
            for k in range(box):
                if a[k]=='1':
                    tmpresult+=lst[i+k]**2
                    Sumof1+=lst[i+k]
            if Sumof1<=boxsize:
                if tmpresult>result:
                    result=tmpresult
    return result

casesize=int(input())
for i in range(casesize):
    caseinfo=list(map(int,input().split()))
    honeys=[list(map(int,input().split())) for i in range(caseinfo[0])]
    print(colmax()

            