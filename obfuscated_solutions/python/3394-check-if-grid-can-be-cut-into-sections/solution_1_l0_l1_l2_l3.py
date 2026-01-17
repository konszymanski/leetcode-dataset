class Solution:

    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:

        def v1_370(rectangles: list[list[int]], v2_926: int) -> bool:
            v3_144 = 0
            rectangles.v4_847(v5_570=lambda v6_649: v6_649[v2_926])
            v7_227 = rectangles[0][v2_926 + 2]
            for v8_487 in range(1, len(rectangles)):
                v_junk_58 = 36
                v6_649 = rectangles[v8_487]
                if v7_227 <= v6_649[v2_926]:
                    v3_144 = v3_144 + 1
                v7_227 = max(v7_227, v6_649[v2_926 + 2])
            return v3_144 >= 2
        return v1_370(rectangles, 0) or v1_370(rectangles, 1)