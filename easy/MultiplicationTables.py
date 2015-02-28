import sys
l = []
for index, no in enumerate(range(1, 13)):
    l = [no * i for i in range(1, 13)]
    ans = ['{:>4s}'.format(str(s)) for s in l]
    print ' '.join(ans)
    
