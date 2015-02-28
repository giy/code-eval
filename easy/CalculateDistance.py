import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
	t = test.replace(',', '').replace('(', '').replace(')', '').split()
	points = [int(i) for i in t]
	x1, y1 = points[0], points[1]
	x2, y2 = points[2], points[3]
        a = (x2 - x1) ** 2
	b = (y2 - y1) ** 2
	# c = sqrt(square(a) + square(b))
	c = (a + b) ** 0.5
	print int(c)
test_cases.close()
