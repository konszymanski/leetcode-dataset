class Solution:
    def garbageCollection(self, garbage, travel):
        v1_754, v2_214, v3_125 = False, False, False
        v4_859 = len(garbage[0])
        for v5_381 in range(len(garbage)  -  1, 0,  - 1):
            v1_754 |= "M" in garbage[v5_381]
            v2_214 |= "P" in garbage[v5_381]
            v3_125 |= "G" in garbage[v5_381]
            v4_859  +=  travel[v5_381 - 1] * (int(v1_754) + int(v2_214)  +  int(v3_125))  +  len(garbage[v5_381])
        return v4_859
