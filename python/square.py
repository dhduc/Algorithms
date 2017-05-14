#!/usr/bin/python
print 'Determine that number is square number'

number = int(raw_input('Your number: '))
isSquare = False
result = ''

if number <= 0 :
	isSquare = False
else :
	for i in range(1, number + 1) :
		if i*i == number :
			isSquare = True
			break

if isSquare :
	result = 'square number'
else :
	result = 'not square number'

print str(number) + ' is ' + result

exit