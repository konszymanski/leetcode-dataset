class Solution:
    def garbageCollection(self, garbage, travel):
        
        for i in range(1, len(travel)):
            travel[i] = travel[i - 1] + travel[i]

        
        garbageLastPos = {}
        ans = 0
        for i in range(len(garbage)):
            for c in garbage[i]:
                garbageLastPos[c] = i
            ans += len(garbage[i])

        garbageTypes = "MPG"
        for c in garbageTypes:
            
            ans += (
                0
                if garbageLastPos.get(c, 0) == 0
                else travel[garbageLastPos.get(c) - 1]
            )

        return ans