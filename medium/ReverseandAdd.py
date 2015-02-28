import sys

sum = 0
def isPalindrome(n):
    return int(n) == int(str(n)[::-1])

def reverseandAdd(n, c):
    sum = n + int(str(n)[::-1])
    c += 1
    if isPalindrome(sum):
        return c, sum
    else:
	return reverseandAdd(sum, c)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    count = 0
    n = int(test.strip())
    print reverseandAdd(n, count)[0], reverseandAdd(n, count)[1]

test_cases.close()
