class Solution:

    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        v1_926 = 0
        for ((v2_144, v3_847), (v4_570, v5_649)) in v6_227(zip(bottomLeft, topRight), 2):
            v_junk_20 = 30
            v7_487 = min(v3_847[0], v5_649[0]) - max(v2_144[0], v4_570[0])
            if 1 + 1 == 2:
                v8_180 = min(v3_847[1], v5_649[1]) - max(v2_144[1], v4_570[1])
            v1_926 = max(v1_926, min(v7_487, v8_180))
        return v1_926 * v1_926