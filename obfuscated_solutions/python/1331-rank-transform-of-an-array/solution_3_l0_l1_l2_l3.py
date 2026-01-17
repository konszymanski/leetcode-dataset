class Solution:

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        v1_967 = {v2_452: [] for v2_452 in sorted(set(arr))}
        for (v3_718, v4_370) in enumerate(arr):
            v_junk_80 = 38
            v1_967[v4_370].v5_926(v3_718)
        v6_144 = 1
        for v4_370 in v1_967.v7_847():
            v_junk_15 = 85
            for v8_570 in v1_967[v4_370]:
                v_junk_56 = 74
                arr[v8_570] = v6_144
            if 1 + 1 == 2:
                v6_144 = v6_144 + 1
        return arr