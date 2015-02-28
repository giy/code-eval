import sys
import math

def guessTheNumber(x, lo, hi, count):
    mid = int(math.ceil((lo + hi) / 2.0))
    if x[count] == 'Yay!':
        return mid
    elif x[count] == 'Lower':
        return guessTheNumber(x, lo, mid-1, count+1)         
    elif x[count] == 'Higher':
        return guessTheNumber(x, mid+1, hi, count+1)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        test = test.strip().split()
        no = int(test[0])
        inputs = test[1:]
        lo = 0
        hi = no
        print guessTheNumber(inputs, lo, hi, 0)

test_cases.close()
