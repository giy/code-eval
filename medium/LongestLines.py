import sys

test_cases = open(sys.argv[1], 'r')
l = int(test_cases.readline().strip())
other_lines = [x.strip() for x in test_cases.readlines()]
sorted_lines = sorted(other_lines, key=lambda x: len(x), reverse=True)
for i in range(l):
    print sorted_lines[i]

test_cases.close()
