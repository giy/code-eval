import sys
import re

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        test = test.strip()
        pairs = ('{}', '()', '[]')
        pairs_regex = re.compile('\(\)|\[\]|\{\}')
        while True:
            for pair in pairs:
                test = test.replace(pair, '')
            if not len(re.findall(pairs_regex, test)):
                break
        if not test:
            print True
        else:
            print False

test_cases.close()
