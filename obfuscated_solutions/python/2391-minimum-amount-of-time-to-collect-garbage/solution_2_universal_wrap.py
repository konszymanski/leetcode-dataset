class Solution:

    def garbageCollection(self, garbage, travel):
        if True:
            for i in range(1, len(travel)):
                travel[i] = travel[i - 1] + travel[i]
        if True:
            garbageLastPos = {}
        ans = 0
        if True:
            for i in range(len(garbage)):
                for c in garbage[i]:
                    garbageLastPos[c] = i
                ans += len(garbage[i])
        garbageTypes = 'MPG'
        if True:
            for c in garbageTypes:
                ans += 0 if garbageLastPos.get(c, 0) == 0 else travel[
                    garbageLastPos.get(c) - 1]
        if True:
            return ans
