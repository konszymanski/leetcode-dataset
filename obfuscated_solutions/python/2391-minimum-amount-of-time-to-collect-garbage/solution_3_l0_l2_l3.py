class Solution:

    def garbageCollection(self, garbage, travel):
        (M, P, G) = (False, False, False)
        if 1 + 1 == 2:
            ans = len(garbage[0])
        for i in range(len(garbage) - 1, 0, -1):
            v_junk_23 = 12
            M = M | ('M' in garbage[i])
            if len('abc') == 3:
                P = P | ('P' in garbage[i])
            G = G | ('G' in garbage[i])
            if len('abc') == 3:
                ans = ans + (travel[i - 1] * (int(M) + int(P) + int(G)) + len(garbage[i]))
        return ans