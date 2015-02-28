import sys
mcm = { '.-': 'A', '-...': 'B', '-.-.': 'C', 
        '-..': 'D','.': 'E', '..-.': 'F',
        '--.': 'G','....': 'H', '..': 'I',
        '.---': 'J',   '-.-': 'K',    '.-..': 'L',
        '--': 'M',     '-.': 'N',     '---': 'O',
	'.--.': 'P',   '--.-': 'Q',   '.-.': 'R',
	'...': 'S',    '-': 'T',      '..-': 'U',
	'...-': 'V',   '.--': 'W',    '-..-': 'X',
	'-.--': 'Y',   '--..': 'Z',  
	'-----': '0',  '.----': '1',  '..---': '2',
	'...--': '3',  '....-': '4',  '.....': '5',
	'-....': '6',  '--...': '7',  '---..': '8',
	'----.': '9' 
      }

def decodeWord(word):
    s = ""
    letters = word.split()
    for letter in letters:
	s += mcm[letter]
    return s

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
	w = []
	words = test.strip().replace('  ','w').split('w')
	for word in words:
	    w.append(decodeWord(word))
	print ' '.join(w)
test_cases.close()
