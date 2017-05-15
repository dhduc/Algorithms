#!/usr/bin/python
print 'Display the digits of number'

number = int(raw_input('Your number: '))
digits = []
result = ''

while number % 10 != 0:
	digits.append(number % 10)
	number = number / 10

for digit in reversed(digits):
	result += ' ' + str(digit)

print 'The digits of ' + str(number) + ' is' + result