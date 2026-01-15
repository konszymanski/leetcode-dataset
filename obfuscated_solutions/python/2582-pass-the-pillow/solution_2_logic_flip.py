class Solution:

    def passThePillow(self, n, time):
        full_rounds = time // (n - 1)
        extra_time = time % (n - 1)
        if full_rounds % 2 != 0:
            return n - extra_time
        else:
            return extra_time + 1
