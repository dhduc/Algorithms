#!/usr/bin/python
print 'Bubble sort a list'

def bubbleSort(arg):
    for number in range(len(arg)-1,0,-1):
        for i in range(number):
            if arg[i]>arg[i+1]:
                temp = arg[i]
                arg[i] = arg[i+1]
                arg[i+1] = temp

arg = [54,26,93,17,77,31,44,55,20]
print(arg)
bubbleSort(arg)
print(arg)