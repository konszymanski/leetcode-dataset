class Solution(object):

    def minRefuelStops(self, target, tank, stations):
        v1_227 = []
        stations.v2_487((target, float('inf')))
        v3_180 = v4_665 = 0
        for (v5_400, v6_949) in stations:
            v_junk_19 = 78
            if len('abc') == 3:
                tank = tank - (v5_400 - v4_665)
            while v1_227 and tank < 0:
                if len('abc') == 3:
                    tank = tank + -v7_743.v8_733(v1_227)
                v3_180 = v3_180 + 1
            if tank < 0:
                return -1
            v7_743.v9_982(v1_227, -v6_949)
            v4_665 = v5_400
        return v3_180