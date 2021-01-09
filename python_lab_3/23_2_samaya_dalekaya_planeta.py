from math import pi


def find_farthest_orbit(arr):
    ellipses = [pi * elem[0] * elem[1] for elem in arr]
    max_ell = max(ellipses)
    index = ellipses.index(max_ell)
    return arr[index]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
