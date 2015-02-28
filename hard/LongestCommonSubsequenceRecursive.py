import sys

def lcs(xstr, ystr):
    if not xstr or not ystr:
        return ""
    x, xs, y, ys = xstr[0], xstr[1:], ystr[0], ystr[1:]
    if x == y:
        return x + lcs(xs, ys)
    else:
        return max(lcs(xstr, ys), lcs(xs, ystr), key=len)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip().split(';')
	xstr = line[0]
	ystr = line[1]
	print lcs(xstr, ystr)
test_cases.close()
