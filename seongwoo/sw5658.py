for t in range(int(input())):
    n,k=list(map(int,input().split()))
    num=input()
    onenum=n//4
    allnum=[]
    for i in range(n-onenum+1):
        changednum=int(num[i:i+onenum],16)
        allnum.append(changednum)
    for m in range(onenum-1):
        changednum=int(num[i+1+m:]+num[:m+1],16)
        allnum.append(changednum)
    allnum=list(set(allnum))
    allnum.sort()
    allnum.reverse()
    print(f'#{t+1} {allnum[k-1]}')

        
