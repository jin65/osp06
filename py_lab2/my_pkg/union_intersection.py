#!/usr/bin/python
import re
def union(x, y):
	x=x.rstrip(']')
	x=x.lstrip('[')
	x=x.replace(" ", "")
	list1=x.split(',')
	y=y.rstrip(']')
	y=y.lstrip('[')
	y=y.replace(" ", "")
	list2=y.split(',')
	set1=set(list1)
	set2=set(list2)
	result=list(set1|set2)
	result.sort()
	return result 

def intersection(x,y):
	x=x.rstrip(']')
	x=x.lstrip('[')
	x=x.replace(" ", "")
	list1=x.split(',')
	y=y.rstrip(']')
	y=y.lstrip('[')
	y=y.replace(" ", "")
	list2=y.split(',')
	set1=set(list1)
	set2=set(list2)
	result=list(set1&set2)
	result.sort()
	return result
	
if __name__=='__main__':
	print("union and intersection of set")
