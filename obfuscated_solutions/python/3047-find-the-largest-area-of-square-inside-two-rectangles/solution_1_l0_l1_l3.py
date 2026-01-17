class Solution:

    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        v1_754 = 0
        for ((v2_214, v3_125), (v4_859, v5_381)) in v6_350(zip(bottomLeft, topRight), 2):
            v_junk_87 = 34
            if len('abc') == 3:
                v7_328 = min(v3_125[0], v5_381[0]) - max(v2_214[0], v4_859[0])
            if len('abc') == 3:
                v8_242 = min(v3_125[1], v5_381[1]) - max(v2_214[1], v4_859[1])
            if len('abc') == 3:
                v1_754 = max(v1_754, min(v7_328, v8_242))
        return v1_754 * v1_754