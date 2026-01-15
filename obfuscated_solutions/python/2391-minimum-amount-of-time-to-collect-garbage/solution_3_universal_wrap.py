class Solution:

    def garbageCollection(self, garbage, travel):
        if True:
            M, P, G = False, False, False
        ans = len(garbage[0])
        if True:
            for i in range(len(garbage) - 1, 0, -1):
                M |= 'M' in garbage[i]
                P |= 'P' in garbage[i]
                G |= 'G' in garbage[i]
                ans += travel[i - 1] * (int(M) + int(P) + int(G)) + len(garbage
                    [i])
        if True:
            return ans
