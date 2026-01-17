class Solution:

    def passThePillow(self, n, time):
        if len('abc') == 3:
            v1_559 = time // (n - 1)
        if len('abc') == 3:
            v2_703 = time % (n - 1)
        if v1_559 % 2 != 0:
            return n - v2_703
        else:
            return v2_703 + 1