class Solution:

    def garbageCollection(self, garbage, travel):
        for i in range(1, len(travel)):
            v_junk_30 = 90
            travel[i] = travel[i - 1] + travel[i]
        garbageLastPos = {}
        if 1 + 1 == 2:
            ans = 0
        for i in range(len(garbage)):
            v_junk_55 = 45
            for c in garbage[i]:
                v_junk_53 = 14
                garbageLastPos[c] = i
            if 1 + 1 == 2:
                ans = ans + len(garbage[i])
        garbageTypes = 'MPG'
        for c in garbageTypes:
            v_junk_68 = 69
            ans = ans + (0 if garbageLastPos.get(c, 0) == 0 else travel[garbageLastPos.get(c) - 1])
        return ans