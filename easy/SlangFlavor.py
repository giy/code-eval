import sys
import re

slang = [", yeah!",", this is crazy, I tell ya.",", can U believe this?",", eh?",", aw yea.",", yo.","? No way!",". Awesome!"]
index = 0
count = 0

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        test = test.strip()
        sentences = [x.strip() for x in re.split('[\.!\?]', test) if len(x) > 0]
        line = []
        for s in sentences:
            if count % 2 != 0:
                line.append(s + slang[index])
                index = (index + 1) % len(slang)
            else:
                punctuation = test[test.find(s) + len(s)]
                line.append(s + punctuation)
            count += 1
        print ' '.join(line)                                                                                                                                                                                                
 
            
test_cases.close()
