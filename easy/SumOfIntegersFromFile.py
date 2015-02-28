import sys
test_cases = open(sys.argv[1], 'r')
sum = 0
for test in test_cases:
    if test:
        no = int(test.strip('\r\n'))
        sum += no
print sum
test_cases.close()
