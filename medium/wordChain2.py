nations = ['albania','andorra','austria','belarus','belgium','bosnia and herzegovina',
      'bulgaria','croatia','czech republic','denmark','estonia',  
      'finland','france','germany','greece','hungary',
      'iceland','ireland','italy','latvia','liechtenstein','lithuania','luxembourg',
      'macedonia','malta','moldova','monaco','montenegro','netherlands', 
      'norway','poland','portugal','romania','russia',  
      'san marino','serbia','slovakia','slovenia','spain','sweden', 'switzerland',
      'ukraine','united kingdom','vatican city']

result = []

def chain(start, countries):
    result.append(start)
    remaining = list(countries)
    del remaining[remaining.index(start)]
    possibilities = [x for x in remaining if start[-1] == x[0]]
    maxchain = []
    for c in possibilities:
	print c, remaining
        l = chain(c, remaining)
        if len(l) > len(maxchain):
	    maxchain = l
	    print maxchain
    return [start] + maxchain

print chain('spain', nations)
