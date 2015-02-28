import sys
from datetime import datetime
def timeDeltaToTime(s):
    hours = s//3600
    s = s - (hours * 3600)
    minutes = s//60
    seconds= s - (minutes * 60)
    return "%s:%s:%s" %(format(hours,'02'), format(minutes,'02'), format(seconds,'02'))

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        line = test.split()
	fmt = "%H:%M:%S"
	first = datetime.strptime(line[0],fmt)
	second = datetime.strptime(line[1], fmt)
        seconds = abs((first - second).total_seconds())
        print timeDeltaToTime(int(seconds))
test_cases.close()
