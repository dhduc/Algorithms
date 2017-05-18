#!/usr/bin/python
print 'Swap two numbers'

def swap_temp(arg) :
	temp = arg[0]
	arg[0] = arg[1]
	arg[1] = temp

def swap_direct(arg) :
	arg[0] = arg[0] + arg[1]
	arg[1] = arg[0] - arg[1]
	arg[0] = arg[0] - arg[1]

arg = [12, 25]
print(arg)
swap_direct(arg)
print(arg)	