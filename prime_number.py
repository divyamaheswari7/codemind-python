N=int(input())
i=1
cnt=0
while i<=N:
    if N%i==0:
        cnt+=1
    i+=1
if cnt==2:
    print("prime")
else:
    print("not a prime")