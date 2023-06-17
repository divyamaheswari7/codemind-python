a=int(input())
for i in range(1,a+1):
    x=int(input())
    t=list(map(int,input().split()))
    c=0
    for i in t:
        if i%2==1:
            c+=1
    print(c//2)