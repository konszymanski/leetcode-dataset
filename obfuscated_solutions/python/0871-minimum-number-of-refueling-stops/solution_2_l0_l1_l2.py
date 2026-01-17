class Solution(object):

    def minRefuelStops(self, target, tank, stations):
        v1_754 = []
        stations.v2_214((target, float('inf')))
        v3_125 = v4_859 = 0
        for (v5_381, v6_350) in stations:
            tank = tank - (v5_381 - v4_859)
            while v1_754 and tank < 0:
                tank = tank + -v7_328.v8_242(v1_754)
                v3_125 = v3_125 + 1
            if tank < 0:
                return -1
            v7_328.v9_854(v1_754, -v6_350)
            v4_859 = v5_381
        return v3_125