def printDigit(n):
    if (n == 0):
        return 
    printDigit(n // 10)
    print(n % 10,end=" ")
T = int(input())
for i in range(T):
    N = int(input())
    if N !=0:
        printDigit(N)
        print()
    else :
        print ("0")
