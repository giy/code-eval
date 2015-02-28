import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        xua, yua, xla, yla, xub, yub, xlb, ylb = (int(i) for i in test.split(','))
        range_x_a = set(xrange(xua, xla + 1))
        range_y_a = set(xrange(yla, yua + 1))
        range_x_b = set(xrange(xub, xlb + 1))
        range_y_b = set(xrange(ylb, yub + 1))
        print True if (range_x_a & range_x_b) and (range_y_a & range_y_b) else False
test_cases.close()
