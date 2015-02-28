import sys
import re
def repetitions(s):
    r = re.compile(r"(.+?)\1+")
    for match in r.finditer(s):
        yield (match.group(1), len(match.group(0))/len(match.group(1)))

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.strip()
        ans = list(repetitions(line))
	if ans:
	    min = 300
	    for i in ans:
		if len(i) < min:
                    min = len(i[0])
            print min
	else:
	    print len(line)
test_cases.close()
