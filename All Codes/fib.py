def Fib(n):
    n1=0
    n2=1
    sum=0
    for i in range(1,n+1):
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
n=int(input('entera number'))        
Fib(n)
    