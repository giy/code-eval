import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().split()
    number_of_doors = int(test[0])
    number_of_iterations = int(test[1])
    
    doors = [False] * number_of_doors
    for i in xrange(number_of_iterations - 1):
        for j in xrange(1, number_of_doors, 2):
	    doors[j] = True
	for j in xrange(2, number_of_doors, 3):
	    doors[j] = not doors[j]

    doors[-1] = not doors[-1]
    total = 0
    for count in range(len(doors)):
        if doors[count] == False:
	    total += 1
    print total

test_cases.close()
