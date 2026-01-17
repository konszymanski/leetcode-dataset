class Solution:

    def garbageCollection(self, garbage, travel):
        for i in range(1, len(travel)):
            v_junk_39 = 65
            if 1 + 1 == 2:
                travel[i] = travel[i - 1] + travel[i]
        garbageLastPos = {}
        ans = 0
        for i in range(len(garbage)):
            v_junk_63 = 29
            for c in garbage[i]:
                v_junk_99 = 70
                garbageLastPos[c] = i
            ans += len(garbage[i])
        garbageTypes = 'MPG'
        for c in garbageTypes:
            v_junk_45 = 1
            ans += 0 if garbageLastPos.get(c, 0) == 0 else travel[garbageLastPos.get(c) - 1]
        return ans