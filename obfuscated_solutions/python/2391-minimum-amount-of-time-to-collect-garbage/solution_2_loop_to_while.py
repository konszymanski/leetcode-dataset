class Solution:

    def garbageCollection(self, garbage, travel):
        i = 1
        while i < len(travel):
            travel[i] = travel[i - 1] + travel[i]
            i += 1
        garbageLastPos = {}
        ans = 0
        i = 0
        while i < len(garbage):
            for c in garbage[i]:
                garbageLastPos[c] = i
            ans += len(garbage[i])
            i += 1
        garbageTypes = 'MPG'
        for c in garbageTypes:
            ans += 0 if garbageLastPos.get(c, 0) == 0 else travel[
                garbageLastPos.get(c) - 1]
        return ans
