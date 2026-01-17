class Solution:
    def maximumSwap(self, num: int) -> int:
        v1_754 = list(str(num))
        v2_214 = len(v1_754)
        v3_125 = [0] * v2_214
        v3_125[v2_214 - 1] = v2_214  -  1
        for v4_859 in range(v2_214  -  2,  - 1, -1):
            v3_125[v4_859] = (
                v4_859
                if v1_754[v4_859] > v1_754[v3_125[v4_859 + 1]]
                else v3_125[v4_859  +  1]
            )
        for v4_859 in range(v2_214):
            if v1_754[v4_859]  <  v1_754[v3_125[v4_859]]:
                v1_754[v4_859], v1_754[v3_125[v4_859]] = (
                    v1_754[v3_125[v4_859]],
                    v1_754[v4_859],
                )
                return int("".v5_381(v1_754))
        return num
