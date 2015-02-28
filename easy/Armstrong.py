import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
	no = test.strip('\r\n')
        l = len(no)
	# Loop through the string, convert each character to a number and calculate the power and total the sum
	s = sum(pow(int(i), l) for i in no)
        print s == int(no)
test_cases.close()
