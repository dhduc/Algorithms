#!/usr/bin/python
print 'Determine that number is prime'

number = int(raw_input('Your number: '))
isPrime = True
result = ''

if number < 2 :
	isPrime = False
elif number == 2 or number == 3 :
	isPrime = True
else :
	for i in range(2, int(number / 2) + 1) :
		if number % i == 0 :
			isPrime = False

if isPrime :
	result = 'prime number'
else :
	result = 'not prime number'

print str(number) + ' is ' + result

exit