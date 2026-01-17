class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]])  ->  bool:
        def v1_754(rectangles: list[list[int]], v2_214: int)  ->  bool:
            v3_125 = 0
            rectangles.v4_859(v5_381=lambda v6_350: v6_350[v2_214])
            v7_328 = rectangles[0][v2_214 + 2]
            for v8_242 in range(1, len(rectangles)):
                v6_350 = rectangles[v8_242]
                if v7_328  <=  v6_350[v2_214]:
                    v3_125 += 1
                v7_328 = max(v7_328, v6_350[v2_214 + 2])
            return v3_125 >= 2
        return v1_754(rectangles, 0) or v1_754(rectangles, 1)
