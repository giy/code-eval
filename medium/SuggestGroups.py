import sys
from collections import Counter

f = {}
h = {}
res = []

def findGroups(name):
    total = []
    suggested_groups = []
    friends = f[name].split(',')
    number_of_friends = len(friends)
    hobbies = h[name]
    for i in friends:
        hobbies_of_friend = h[i].split(',')
        total.extend(hobbies_of_friend)
    counter = Counter(total)
    for i in counter:
	if counter.get(i) >= (float)(number_of_friends/2.0):
            if i not in h[name]:
	        suggested_groups.append(i)
    return name, suggested_groups


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
	line = test.strip().split(':')
        name = line[0]
	friends = line[1]
	hobbies = line[2]
	res.append(name)
        f[name] = friends
        h[name] = hobbies

res = sorted(res)
for name in res:
    name, suggested_groups = findGroups(name)
    suggested_groups = ','.join(sorted(suggested_groups))
    if suggested_groups:
        print name + ':' + suggested_groups

test_cases.close()
