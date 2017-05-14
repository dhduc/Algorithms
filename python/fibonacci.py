#!/usr/bin/python
print 'Print the n (amount) first Fibonacci number'

amount = int(raw_input('Your amount: '))
result = ''

def fibR(n) :
	if n == 1 or n == 2:
		return 1
	else :
		return fibR(n - 1) + fibR(n - 2)

def printFibR(n) :
	listNumber = 'Fibonacci list:'
	for i in range(1, n + 1):
		listNumber += ' ' + str(fibR(i))

	print listNumber	

printFibR(amount)		

exit	