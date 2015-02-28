import re
import math
import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

def dist_a_to_b(a, b):
    return math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))

for test in test_cases:
    points_regex = re.compile('\((\d+)?,(\d+)\)')
    points = sorted((int(j[0]), int(j[1])) for j in
                    re.findall(points_regex, test))
    distances_to_check = [(0, 1), (0, 3), (0, 2), (1, 3), (1, 2), (2, 3)]
    distances = set()
    for d in distances_to_check:
        distances.add(dist_a_to_b(points[d[0]], points[d[1]]))
    is_square = False
    if len(distances) == 2:
        is_square = True
    print str(is_square).lower()
        
