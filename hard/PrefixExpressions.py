import sys

stack = []

def do(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '*':
	return first * second
    elif operation == '/':
	return (float)(first)/(float)(second)

def prefixExpressions(l):
    for i in range(len(l)-1,-1,-1):
	if l[i].isdigit():
	    stack.append(int(l[i]))
	else: # if it is an operator
	    operation = l[i]
	    first = stack.pop()
	    second = stack.pop()
	    if operation == '+' or operation == '*' or operation == '/':
	        third = do(first, second, operation)
	        stack.append(third)
	    else:
		 continue
    total = stack.pop()
    return int(total)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    line = test.strip().split()
    print prefixExpressions(line)
test_cases.close()
