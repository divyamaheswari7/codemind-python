n=int(input())
sum_n=0  
for i in range(1,n):  
    if (n%i==0):  
        sum_n=sum_n+i  
if(sum_n==n):  
    print("True")  
else:  
    print("False")