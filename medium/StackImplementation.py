import sys

class myStack:
    def __init__(self):
        self.container = []

    def push(self, no):
        self.container.append(no)

    def isEmpty(self):
	return len(self.container) == 0

    def pop(self):
	return self.container.pop()

    def size(self):
	return len(self.container)
         

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        test = test.strip().split()
        s = myStack()
	for i in test:
	    s.push(i)
	l = []
	i = 0
	while not s.isEmpty():
	    if i%2 == 0:
	        l.append(s.pop())
	    else:
		s.pop()
	    i += 1
	print ' '.join(l)

test_cases.close()
