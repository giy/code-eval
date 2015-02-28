import sys

def sum_digits(no):
    sum = 0
    for i in str(no):
        sum += int(i)
    return sum

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        res = []
        x = test.strip()[::-1]
	for i in x:
	    if i.isdigit():
	        res.append(int(i))
	for index,i in enumerate(res):
	    if index % 2 == 1:
                res[index] = 2*res[index] 
                if res[index] > 9:
		    res[index] = sum_digits(res[index])

        result = sum(res)
        if not result % 10:
	    print 1
	else:
	    print 0

test_cases.close()
