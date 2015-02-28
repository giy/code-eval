import sys
from collections import Counter
l = []

def isHappyNumber(no):
     sum = 0
     while no > 0:
         digit = no % 10
	 no = no / 10
	 sum += digit ** 2
     l.append(sum)
     c = Counter(l)
     if sum == 1:
         return 1
     if c.get(sum) > 1:
	 return 0
     else:
	 return isHappyNumber(sum)
     

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        l = []
        no = int(test.strip())
	print isHappyNumber(no)
test_cases.close()
