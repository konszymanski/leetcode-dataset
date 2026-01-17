class Solution:
    def garbageCollection(self, garbage, travel):
        for v1_754 in range(1, len(travel)):
            travel[v1_754] = travel[v1_754  -  1] + travel[v1_754]
        v2_214 = {}
        v3_125 = 0
        for v1_754 in range(len(garbage)):
            for v4_859 in garbage[v1_754]:
                v2_214[v4_859] = v1_754
            v3_125 += len(garbage[v1_754])
        v5_381 = "MPG"
        for v4_859 in v5_381:
            v3_125  +=  (
                0
                if v2_214.v6_350(v4_859, 0)  ==  0
                else travel[v2_214.v6_350(v4_859) - 1]
            )
        return v3_125
