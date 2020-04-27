#!/usr/bin/python
import my_pkg.bin_conversion as bin
import my_pkg.union_intersection as set_cal
if __name__=='__main__':
	menu=0
	while(menu!=3):
		menu=int(input("Select menu: 1)conversion 2)union/intersection 3)exit ?"))
		if(menu==1):
			value=input("input binary number:")
			print("=>OCT>",bin.octal(value))
			print("=>DEC>",bin.decimal(value))
			print("=>HEX>",bin.hexadecimal(value))
		elif(menu==2):
			s1=input("1st list:")
			s2=input("2nd list:")
			print("=>union", set_cal.union(s1,s2))
			print("=>intersection", set_cal.intersection(s1,s2))
	print("exit the program...")
