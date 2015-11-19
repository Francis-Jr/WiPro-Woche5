__author__ = 'jakobunfried'

"""Sinus durch Taylor"""

import math.factorial() as fact()
import math.pi as pi


def my_sin(a, n):
    sign = 1.
    buf = 0.0
    for i in range(1, n+1, 2):
        buf += a**i/fact(i)*sign
        sign *= -1.
    return buf


print my_sin(pi/4, 5)
