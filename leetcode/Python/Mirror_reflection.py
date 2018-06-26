import numpy as np
from fractions import gcd

class Solution(object):
    def mirrorReflection(self, p, q):
        g = gcd(p, q)
        p = (p / g) % 2
        q = (q / g) % 2

        return 1 if p and q else 0 if p else 2

if __name__ == "__main__":
	p = 5; q = 4
	ans = sol.mirrorReflection(p, q)
	print ans