def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 0
    elif n>=2:
        a=0
        b=1
        print(a,end=" ")
        print(b,end=" ")
        for i in range(3,n+1):
            c=a+b
            a=b
            b=c
            print(c,end=" ")
        return c
    
n=int(input("Enter the number of terms:"))
print("Fibonacci series:")
fibonacci(n)