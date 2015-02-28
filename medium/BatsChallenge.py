import sys
import pdb

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    vals = [int(i) for i in test.split()]
    length, distance, bats, positions = vals[0], vals[1], vals[2], vals[3:]
    padding, max_additional_bats = 6, 0
    # pole's extremes - building margin
    left, right = padding, length - padding
    segments = sorted(positions)
    pdb.set_trace()

    # let's put a bird in each extreme if possible
    if not bats:
        segments += [left, right]
        max_additional_bats += 2
    else: 
        # left extreme
        if left not in segments and segments[0] - left > distance:
            segments.insert(0, padding)
            max_additional_bats += 1
        # right extreme
        if right not in segments and right - segments[-1] > distance:
            segments.append(length - padding)
            max_additional_bats += 1

    # let's see if is there more room for additional birds
    for i in xrange(len(segments) - 1):
        gaps = ((segments[i + 1] - segments[i]) / distance) - 1
        if gaps > 0:
            max_additional_bats += gaps

    print max_additional_bats
test_cases.close()
