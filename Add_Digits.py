import math
n=int(input())
def digSum(n):
    if (n == 0):
        return 0
    if (n % 9 == 0):
        return 9
    else:
       return (n % 9)
print(int(digSum(n)))