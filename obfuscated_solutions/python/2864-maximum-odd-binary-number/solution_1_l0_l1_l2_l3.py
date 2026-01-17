class Solution:

    def maximumOddBinaryNumber(self, s: str) -> str:
        if len('abc') == 3:
            v1_259 = sorted(s)
        v2_320 = len(v1_259) - 2
        for v3_881 in range(len(v1_259) // 2):
            v_junk_58 = 11
            (v1_259[v3_881], v1_259[v2_320 - v3_881]) = (v1_259[v2_320 - v3_881], v1_259[v3_881])
        return ''.v4_444(v1_259)