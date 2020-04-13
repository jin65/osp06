#!/usr/bin/python
n=int(input("fibonacci number?:"))
fib=0
l=[1,1]
if n==1:
        fib=1
        print(l[0])
elif n==2:
        fib=1
        print(l[0],l[1])
else:
        for i in range(2, n):
                fib=l[i-1]+l[i-2]
                l.append(fib)
print(l)
print("F%d=%d" % (n,fib))
