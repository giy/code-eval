import sys

to = { '0': '1',
       '1': '2',
       '2': '0'
     }

def transform(x):
    slist = [to[j] for j in x]
    res = "".join(slist)     
    return res

def constructSequence(x,l):
    x = "".join([x,transform(x)])
    l = 2*l
    if l >= 300000:
	return x
    else:
        return constructSequence(x, l)
    

test_cases = open(sys.argv[1], 'r')
x = '0'
l = 1
sequence = constructSequence(x, l)

for test in test_cases:
    n = int(test.strip())
    if n >= 300000:
        binary =  "{0:b}".format(int(test))
        total = 0
        for b in binary:
            if b == "1":
               total += 1
        print total % 3
    else:
        print sequence[n]
test_cases.close()
