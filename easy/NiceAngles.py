import sys
def dminsec(decdegrees):
    degrees = int(decdegrees)
    temp = 60*(decdegrees - degrees)
    min = int(temp)
    seconds = 60*(temp - min)
    return degrees, format( min, '02d'), format(int(seconds), '02d')

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        decdegrees = float(test.strip())
	degrees, min, seconds = dminsec(decdegrees)
        print str(degrees) + "." + str(min) + "'" + str(seconds) + "\""
test_cases.close()
