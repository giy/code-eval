import sys
from ast import literal_eval
import math

def point_isinside_circle(x, y, r, center_x, center_y):
    dist = math.sqrt(((x - center_x) ** 2) + ((y - center_y) ** 2))
    return str(dist < r).lower()


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().split(';')
    # The point is inside if (x - xcenter)**2 + (y - ycenter)**2 < r**2
    center = literal_eval(test[0].strip().split(':')[1].strip())
    r = literal_eval(test[1].strip().split(':')[1].strip())
    p = literal_eval(test[2].strip().split(':')[1].strip())
    center_x, center_y = float(center[0]), float(center[1])
    x, y = float(p[0]), float(p[1])
    r = float(r)
    print point_isinside_circle(x, y, r, center_x, center_y)

test_cases.close()
