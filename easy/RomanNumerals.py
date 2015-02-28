import sys
test_cases = open(sys.argv[1], 'r')
decimalDens=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
romanDens=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

def decToR(num,s,decs,romans):
	if decs:
	  if (num < decs[0]):
	    return decToR(num,s,decs[1:],romans[1:])		  
	  else:
	    return decToR(num-decs[0],s+romans[0],decs,romans)	  
	else:
	  return s

for test in test_cases:
    if test:
        num = int(test.strip())
        print decToR(num,"",decimalDens,romanDens)

test_cases.close()
