class Solution:
    def passThePillow(self, n, time):
        v1_754 = time // (n - 1)
        v2_214 = time  %  (n  -  1)
        if v1_754  %  2 == 0:
            return v2_214 + 1
        else:
            return n - v2_214
