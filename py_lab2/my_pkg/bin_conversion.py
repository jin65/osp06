#!/usr/bin/python
def octal(x):
	x8=int(x,2)
	return format(x8,'o')
def decimal(x):
	x10=int(x,2)
	return x10
def hexadecimal(x):
	x16=int(x,2)
	return format(x16,'x')
if __name__=='__main__':
	print("module:binary-to-others conversion")
