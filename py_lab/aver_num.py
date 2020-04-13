#!/usr/bin/python
n=int(input("N:"))
sum=0
for i in range(1, n+1):
        num=int(input("input value"+str(i)+": "))
        sum=sum+num
avg=sum/n
print(avg)
