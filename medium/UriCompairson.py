import sys
import re
import urllib
import pdb

test_cases = open(sys.argv[1], 'r')
def appendPortIfNotPresent(hn):
    if not ':' in hn:
        hn = hn + ":80"
    return hn

def comparePathNames(l1, l2):
    if len(l1) != len(l2):
        return False
    res = True
    for i in range(len(l1)):
	x = l1[i]
	y = l2[i]
        match = re.search('%([0-9a-fA-F][0-9a-fA-F])', x)
	if not match:
            x = urllib.quote(x)
        match = re.search('%([0-9a-fA-F][0-9a-fA-F])', y)
        if not match:
	    y = urllib.quote(y)
	if x != y:
	    res = False
            break
    return res

def checkHostNames(hn0, hn1):
        hn0 = appendPortIfNotPresent(hn0)
        hn1 = appendPortIfNotPresent(hn1)
	h0 = hn0.split(':')[0].lower()
	p0 = hn0.split(':')[1]
	h1 = hn1.split(':')[0].lower()
	p1 = hn1.split(':')[1]
	if h0 == h1 and p0 == p1:
	    return True
        else:
	    return False

for test in test_cases:
    if test:
        line = test.strip().split(';')
	uri1 = line[0]
	uri2 = line[1]
        match = "^([a-zA-Z]+)://([a-zA-Z0-9.]+):?([0-9]+)?(.*)"
	m1 = re.match(match, uri1)
	m2 = re.match(match, uri2)
	if not m1 or not m2:
            print False
	    continue
        if m1.group(1) != m2.group(1):
	    print False
	    continue
        s1 = m1.group(1) + "://"
	s2 = m2.group(1) + "://"
	uri1_p = uri1.replace(s1,"").split('/')
	uri2_p = uri2.replace(s2,"").split('/')
        hostname_check = checkHostNames(uri1_p[0], uri2_p[0])
	path_check = comparePathNames(uri1_p[1:], uri2_p[1:])
        if hostname_check and path_check:
	    print True
        else:
            print False

test_cases.close()
