import sys

def pascalsTriangle(n_rows):
    results = []
    for i in range(n_rows): 
        row = [1]
        if results:
            last_row = results[-1] 
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        results.append(row) # add the row to the results.
    return results

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        no_rows = int(test.strip())
	for i in pascalsTriangle(no_rows):
            for j in i: 
		print j,
    print 
test_cases.close()
