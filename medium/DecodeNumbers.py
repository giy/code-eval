import sys
import pdb

d = { 'A': 1,
      'B': 2,
      'C': 3,
      'D': 4,
      'E': 5,
      'F': 6,
      'G': 7,
      'H': 8,
      'I': 9,
      'J': 10,
      'K': 11,
      'L': 12,
      'M': 13,
      'N': 14,
      'O': 15,
      'P': 16,
      'Q': 17,
      'R': 18,
      'S': 19,
      'T': 20,
      'U': 21,
      'V': 22,
      'W': 23,
      'X': 24,
      'Y': 25,
      'Z': 26 }

def decodeNumbers(message):
    if len(message) == 1 or len(message) == 0:
        return 1
    possibilities = 0
    num_chars = 1
    while True:
        chars = message[0:num_chars]
	print message, chars, possibilities
        if len(chars) != num_chars:
            break
        if int(chars) > 26:
            break
        possibilities += decodeNumbers(message[num_chars:])
        num_chars += 1
    return possibilities

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    no = test.strip()
    print decodeNumbers(no)
test_cases.close()
