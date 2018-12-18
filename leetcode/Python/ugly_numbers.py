import numpy as np

class Solution:
    def nthUglyNumer(self, n):
        ugly = [0] * (n+1)
        ugly[0] = 1
        i2 = i3 = i5 = 0
        mult_2 = ugly[i2] * 2
        mult_3 = ugly[i3] * 3
        mult_5 = ugly[i5] * 5
        for i in range(1, n + 1):
            ugly[i] = min(mult_2, mult_3, mult_5)

            if ugly[i] == mult_2:
                i2 += 1
                mult_2 = ugly[i2] * 2
            if ugly[i] == mult_3:
                i3 += 1
                mult_3 = ugly[i3] * 3
            else:
                i5 += 1
                mult_5 = ugly[i5] * 5
        return ugly[n]