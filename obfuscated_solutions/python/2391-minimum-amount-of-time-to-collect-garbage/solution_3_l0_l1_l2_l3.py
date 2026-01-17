class Solution:

    def garbageCollection(self, garbage, travel):
        if 1 + 1 == 2:
            (v1_370, v2_926, v3_144) = (False, False, False)
        v4_847 = len(garbage[0])
        for v5_570 in range(len(garbage) - 1, 0, -1):
            v_junk_30 = 48
            v1_370 = v1_370 | ('M' in garbage[v5_570])
            v2_926 = v2_926 | ('P' in garbage[v5_570])
            v3_144 = v3_144 | ('G' in garbage[v5_570])
            v4_847 = v4_847 + (travel[v5_570 - 1] * (int(v1_370) + int(v2_926) + int(v3_144)) + len(garbage[v5_570]))
        return v4_847