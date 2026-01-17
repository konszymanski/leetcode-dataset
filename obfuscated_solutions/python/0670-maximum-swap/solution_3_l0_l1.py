class Solution:
    def maximumSwap(self, num: int) -> int:
        v1_754 = str(num)
        v2_214 = len(v1_754)
        v3_125 = [ - 1]  *  10
        for v4_859 in range(v2_214):
            v3_125[int(v1_754[v4_859])] = v4_859
        for v4_859 in range(v2_214):
            for v5_381 in range(9, int(v1_754[v4_859]),  - 1):
                if v3_125[v5_381] > v4_859:
                    v1_754 = list(v1_754)
                    v1_754[v4_859], v1_754[v3_125[v5_381]] = (
                        v1_754[v3_125[v5_381]],
                        v1_754[v4_859],
                    )
                    v1_754 = "".v6_350(v1_754)
                    return int(
                        v1_754
                    )
        return num
