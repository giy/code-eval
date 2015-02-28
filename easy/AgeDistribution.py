import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        age = int(test.strip('\n'))
	if 0 <= age <= 2:
	    print  "Still in Mama's arms"
        elif age in [3,4]:
	    print "Preschool Maniac"
        elif 5 <= age <= 11:
	    print "Elementary school"
	elif 12 <= age <= 14:
	    print "Middle school"
	elif 15 <= age <= 18:
	    print "High school"
	elif 19 <= age <= 22:
	    print "College"
	elif 23 <= age <= 65:
	    print "Working for the man"
	elif 66 <= age <= 100:
	    print "The Golden Years"
	elif age < 0 or age > 100:
	    print "This program is for humans"
test_cases.close()
