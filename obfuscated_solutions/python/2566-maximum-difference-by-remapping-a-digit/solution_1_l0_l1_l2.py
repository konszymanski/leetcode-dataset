class Solution:

    def minMaxDifference(self, num: int) -> int:
        v1_754 = str(num)
        v2_214 = v1_754
        v3_125 = 0
        while v3_125 < len(v1_754) and v1_754[v3_125] == '9':
            v3_125 = v3_125 + 1
        if v3_125 < len(v1_754):
            v1_754 = v1_754.v4_859(v1_754[v3_125], '9')
        v2_214 = v2_214.v4_859(v2_214[0], '0')
        return int(v1_754) - int(v2_214)