#!/usr/bin/python
print 'Determine that number is prime'

number = int(raw_input('Your number: '))
count = 0
result = ''

for i in range(1, number + 1) :
	if number % i == 0 :
		count = count + 1

if count == 2 :
	result = 'prime number'
else :
	result = 'not prime number'

print str(number) + ' is ' + result

exit