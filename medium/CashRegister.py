import sys

inv = {
         'PENNY': .01,
         'NICKEL': .05,
         'DIME': .10,
         'QUARTER': .25,
         'HALF DOLLAR': .50,
         'ONE': 1.00,
         'TWO': 2.00,
         'FIVE': 5.00,
         'TEN': 10.00,
         'TWENTY': 20.00,
         'FIFTY': 50.00,
         'ONE HUNDRED': 100.00
       }

def find_key(x):
    for key in inv:
	if inv[key] == x:
	    return key
    

def calculate_money(diff):
    val = sorted(inv.values())
    i = 0
    prev = val[0]
    while val[i] <= diff:
        prev = val[i]
	i += 1
	if i == len(val):
	    break
    results.append(find_key(prev))
    diff = float(format(diff-prev, '.2f')) #remaining_change
    if diff > 0:
        return calculate_money(diff)
    return results

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
	results = []
        line = test.strip().split(';')
	pp = float(line[0])
	cash = float(line[1])
	diff = float(format(cash - pp, '.2f'))
        if diff < 0:
	    print "ERROR"	
        elif diff == 0:
	    print "ZERO"
	else:
            print ','.join(calculate_money(diff))
        

test_cases.close()
