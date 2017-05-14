#!/usr/bin/python
print 'Determine that number is perfect number'

number = int(raw_input('Your number: '))
isPerfect = False
result = ''

if number <= 1 :
	isPerfect = False
else :
	sumDivision = 0
	for i in range(1, number) :
		if number % i == 0 :
			sumDivision += i
	if sumDivision == number :
		isPerfect = True
			
if isPerfect :
	result = 'perfect number'
else :
	result = 'not perfect number'


print str(number) + ' is ' + result

exit