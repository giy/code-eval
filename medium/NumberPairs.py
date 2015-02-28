import sys

def findNumberPairs(nos, total):
    result = []
    i = 0
    j = len(nos) - 1
    while i < j:
       x = nos[i]
       y = nos[j]
       if (x + y) == total:
           result.append((x,y))
	   i += 1
	   j -= 1
       elif (x + y) > total:
           j -= 1
       elif (x + y) < total:
	   i += 1
    if result:
        result = ";".join("%s,%s" % tup for tup in result)
    else:
	result = "NULL"
    return result

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip().split(';')
        nos = [int(i) for i in line[0].split(',')]
	total = int(line[1])
        print findNumberPairs(nos, total)
test_cases.close()
