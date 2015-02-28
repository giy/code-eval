rows = [[str(i * j) for i in range(1, 13)] for j in range(1, 13)]

for line in rows:
    for num in line:
        if line.index(num):
	    print ' '*(3 - len(num)) + num,
	else:
	    print ' '*(2 - len(num)) + num,
    print
